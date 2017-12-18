import random
import math
from collections import deque

import tensorflow as tf
import numpy as np

from game.client.user_client import UserClient
from game.common.enums import *

from deep_q import DeepQCombat

## https://github.com/DanielSlater/PyGamePlayer/blob/master/examples/deep_q_pong_player.py
## http://www.danielslater.net/2016/03/deep-q-learning-pong-with-tensorflow.html

# Enumerate combat actions
# unit 1
# 1 - primary attack
# 2 - bomb/spell 1
# 3 - bomb/spell 2
# 4 - bomb/spell 3
# 5 - special ability

# unit 2
# 8 - primary attack
# 9 - bomb/spell 1
# 10 - bomb/spell 2
# 11 - bomb/spell 3
# 12 - special ability

# unit 3
# 15 - primary attack
# 16 - bomb/spell 1
# 17 - bomb/spell 2
# 18 - bomb/spell 3
# 19 - special ability

# unit 4
# 22 - primary attack
# 23 - bomb/spell 1
# 24 - bomb/spell 2
# 25 - bomb/spell 3
# 26 - special ability
NUM_STATES = 77
NUM_ACTIONS = 5
OBSERVATION_STEPS = 5000
MEMORY_SIZE = 50000
FUTURE_REWARD_DISCOUNT = 0.99 # decay of past observations
MINI_BATCH_SIZE = 100
INITIAL_RANDOM_ACTION_PROB = 1.0
FINAL_RANDOM_ACTION_PROB = 0.05
EXPLORE_STEPS = 5000

gamma = 0.99
def discount_rewards(r):
    discounted_r = np.zeros((len(r), len(r[0])))

    running_add = 0

    for i in range(0, r.size):
        ep = r[i]
        for t in reversed(range(0, ep.size)):
            running_add = running_add * gamma + ep[t]
            discounted_r[i][t] = running_add
    return discounted_r

def hot_one_state(index):
    array = np.zeros(NUM_STATES)
    array[index] = 1.
    return array


class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """

        self.quit_on_game_over = False # prevents client from exiting on game end

        self.combat_model = DeepQCombat(1e-3, NUM_STATES, NUM_ACTIONS)

        self.recent_combat = False
        self.reward = 0
        self.past_reward = []

        self.step = 0
        self.e = 0.7
        self.first = True
        self.update_frequency = 50
        self.current_state = []
        self.previous_state = []
        self.terminal = False

        self.loss = [.0]


        self.observations = deque()

        self.last_action = np.zeros(NUM_ACTIONS)
        self.last_action[1] = 1

        self.last_state = np.zeros(NUM_STATES)
        self.probability_of_random_action = INITIAL_RANDOM_ACTION_PROB
        self.time = 0

        self.sess = tf.InteractiveSession()
        self.sess.run(tf.global_variables_initializer())

        self.episode_history = []

        self.previous_health = {
            "unit_1" : 0,
            "unit_2" : 0,
            "unit_3" : 0,
            "unit_4" : 0,
            "monster" : 0,
        }

    def team_name(self):
        print("Sending Team Name")

        return "Team Coffee !@#$$%%^&^**()(*&^%$#"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
                {
                    "name": "a",
                    "class": UnitClass.alchemist
                },
                {
                    "name": "b",
                    "class": UnitClass.brawler
                },
                {
                    "name": "c",
                    "class": UnitClass.pikeman
                },
                {
                    "name": "d",
                    "class": UnitClass.knight
                }
            ]


    def town(self, units, gold, store):
        print()
        print("*"*50)
        print("Town")
        print("*"*50)

        print("Gold: {}".format(gold))


        if store.get_town_number() is 0:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 1)
                store.purchase(unit, 2, ItemType.fire_bomb, 1)

        elif store.get_town_number() is 1:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 2)
                store.purchase(unit, 2, ItemType.fire_bomb, 2)

        elif store.get_town_number() is 3:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 3)
                store.purchase(unit, 2, ItemType.fire_bomb, 3)

        elif store.get_town_number() is 4:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 4)
                store.purchase(unit, 2, ItemType.fire_bomb, 4)


    def room_choice(self, units, options):

        if self.recent_combat:
            self.recent_combat = False
            self.terminal = True



        if len(options) == 1:
            return Direction.forward

        elif len(options) == 2:
            return random.choice([Direction.right, Direction.left])

        else:
            return MessageType.null

    def combat_round(self, monster, units):
        #print()
        #print("*"*50)
        #print("Combat")
        #print("*"*50)
        #print(monster.summary())
        #for u in units:
        #    print(u.summary())

        # sort units alphabetically by name
        units = sorted(units, key=lambda el: el.name)

        if not self.recent_combat:
            self.previous_health["unit_1"] = units[0].current_health
            self.previous_health["unit_2"] = units[1].current_health
            self.previous_health["unit_3"] = units[2].current_health
            self.previous_health["unit_4"] = units[3].current_health
            self.previous_health["monster"] = monster.current_health

            self.recent_combat = True

        else:
            # calculate reward for damage to / from units

            health_diff = self.previous_health["monster"] - monster.current_health
            if health_diff > 0:
                dmg_reward = math.ceil(
                    (
                        (self.previous_health["monster"]/float(monster.health)) -
                        (monster.current_health/float(monster.health))
                    ) * 50)
                #print("health diff ", health_diff, " damage reward", dmg_reward)
                self.reward += dmg_reward
            else:
                #self.reward -= 1
                pass

            self.previous_health["unit_1"] = units[0].current_health
            self.previous_health["unit_2"] = units[1].current_health
            self.previous_health["unit_3"] = units[2].current_health
            self.previous_health["unit_4"] = units[3].current_health
            self.previous_health["monster"] = monster.current_health

        self.recent_combat = True



        self.step += 1

        # Convert current game state into state vector


        self.previous_state = self.current_state

        self.current_state = [

            # unit health
            float(units[0].current_health)/units[0].health,
            float(units[1].current_health)/units[1].health,
            float(units[2].current_health)/units[2].health,
            float(units[3].current_health)/units[3].health,

            #unit weapon types
            float(units[0].primary_weapon.item_type),
            float(units[0].primary_weapon.level),

            float(units[0].bomb_1.item_type if units[0].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[0].bomb_1 is not None else -1),
            float(units[0].bomb_1.level if units[0].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[0].bomb_1 is not None else -1),
            float(units[0].bomb_1_quantity if units[0].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[0].bomb_1 is not None else -1),

            float(units[0].bomb_2.item_type if units[0].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[0].bomb_2 is not None else -1),
            float(units[0].bomb_2.level if units[0].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[0].bomb_2 is not None else -1),
            float(units[0].bomb_2_quantity if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[1].bomb_2 is not None else -1),

            float(units[0].bomb_3.item_type if units[0].unit_class in [UnitClass.rogue]
                   and units[0].bomb_3 is not None else -1),
            float(units[0].bomb_3.level if units[0].unit_class in [UnitClass.rogue]
                   and units[0].bomb_3 is not None else -1),
            float(units[0].bomb_3_quantity if units[0].unit_class in [UnitClass.rogue]
                  and units[0].bomb_3 is not None else -1),

            float(units[0].spell_1.item_type if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_1 is not None else -1),
            float(units[0].spell_1.level if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_1 is not None else -1),

            float(units[0].spell_2.item_type if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_2 is not None else -1),
            float(units[0].spell_2.level if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_2 is not None else -1),

            float(units[0].spell_3.item_type if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_3 is not None else -1),
            float(units[0].spell_3.level if units[0].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[0].spell_3 is not None else -1),


            float(units[1].primary_weapon.item_type),
            float(units[1].primary_weapon.level),

            float(units[1].bomb_1.item_type if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[1].bomb_1 is not None else -1),
            float(units[1].bomb_1.level if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[1].bomb_1 is not None else -1),
            float(units[1].bomb_1_quantity if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[1].bomb_1 is not None else -1),

            float(units[1].bomb_2.item_type if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[1].bomb_2 is not None else -1),
            float(units[1].bomb_2.level if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                   and units[1].bomb_2 is not None else -1),
            float(units[1].bomb_2_quantity if units[1].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[1].bomb_2 is not None else -1),

            float(units[1].bomb_3.item_type if units[1].unit_class in [UnitClass.rogue]
                   and units[1].bomb_3 is not None else -1),
            float(units[1].bomb_3.level if units[1].unit_class in [UnitClass.rogue]
                   and units[1].bomb_3 is not None else -1),
            float(units[1].bomb_3_quantity if units[1].unit_class in [UnitClass.rogue]
                  and units[1].bomb_3 is not None else -1),

            float(units[1].spell_1.item_type if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_1 is not None else -1),
            float(units[1].spell_1.level if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_1 is not None else -1),

            float(units[1].spell_2.item_type if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_2 is not None else -1),
            float(units[1].spell_2.level if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_2 is not None else -1),

            float(units[1].spell_3.item_type if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_3 is not None else -1),
            float(units[1].spell_3.level if units[1].unit_class in
                [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[1].spell_3 is not None else -1),


            float(units[2].primary_weapon.item_type),
            float(units[2].primary_weapon.level),

            float(units[2].bomb_1.item_type if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_1 is not None else -1),
            float(units[2].bomb_1.level if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_1 is not None else -1),
            float(units[2].bomb_1_quantity if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_1 is not None else -1),

            float(units[2].bomb_2.item_type if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_2 is not None else -1),
            float(units[2].bomb_2.level if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_2 is not None else -1),
            float(units[2].bomb_2_quantity if units[2].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[2].bomb_2 is not None else -1),

            float(units[2].bomb_3.item_type if units[2].unit_class in [UnitClass.rogue]
                  and units[2].bomb_3 is not None else -1),
            float(units[2].bomb_3.level if units[2].unit_class in [UnitClass.rogue]
                  and units[2].bomb_3 is not None else -1),
            float(units[2].bomb_3_quantity if units[2].unit_class in [UnitClass.rogue]
                  and units[2].bomb_3 is not None else -1),

            float(units[2].spell_1.item_type if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_1 is not None else -1),
            float(units[2].spell_1.level if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_1 is not None else -1),

            float(units[2].spell_2.item_type if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_2 is not None else -1),
            float(units[2].spell_2.level if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_2 is not None else -1),

            float(units[2].spell_3.item_type if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_3 is not None else -1),
            float(units[2].spell_3.level if units[2].unit_class in
                    [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[2].spell_3 is not None else -1),


            float(units[3].primary_weapon.item_type),
            float(units[3].primary_weapon.level),

            float(units[3].bomb_1.item_type if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_1 is not None else -1),
            float(units[3].bomb_1.level if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_1 is not None else -1),
            float(units[3].bomb_1_quantity if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_1 is not None else -1),

            float(units[3].bomb_2.item_type if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_2 is not None else -1),
            float(units[3].bomb_2.level if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_2 is not None else -1),
            float(units[3].bomb_2_quantity if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_2 is not None else -1),

            float(units[3].bomb_3.item_type if units[3].unit_class in [UnitClass.rogue]
                  and units[3].bomb_3 is not None else -1),
            float(units[3].bomb_3.level if units[3].unit_class in [UnitClass.rogue]
                  and units[3].bomb_3 is not None else -1),
            float(units[3].bomb_3_quantity if units[3].unit_class in [UnitClass.alchemist, UnitClass.rogue]
                  and units[3].bomb_3 is not None else -1),

            float(units[3].spell_1.item_type if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_1 is not None else -1),
            float(units[3].spell_1.level if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_1 is not None else -1),

            float(units[3].spell_2.item_type if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_2 is not None else -1),
            float(units[3].spell_2.level if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_2 is not None else -1),

            float(units[3].spell_3.item_type if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_3 is not None else -1),
            float(units[3].spell_3.level if units[3].unit_class in
                  [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer] and units[3].spell_3 is not None else -1),

            # monster health
            float(monster.current_health)/monster.health,

            # current monster weaknesses
            float( monster.weaknesses[0] if len(monster.weaknesses) >= 1 else -1),
            float( monster.weaknesses[1] if len(monster.weaknesses) >= 2 else -1),
            float( monster.weaknesses[2] if len(monster.weaknesses) >= 3 else -1),
            float( monster.weaknesses[3] if len(monster.weaknesses) >= 4 else -1)

        ]


        # handle first step differently
        if self.last_state is None:
            self.last_state = self.current_state

        self.observations.append((
            self.last_state,
            self.last_action,
            self.reward,
            self.current_state,
            self.terminal
        ))

        if len(self.observations) > MEMORY_SIZE:
            self.observations.popleft()

        if len(self.observations) > OBSERVATION_STEPS:
            self.train()
            self.time += 1

        self.past_reward.append(self.reward)
        avg_reward = np.mean(self.past_reward)

        print("Time:", self.time, "Observations:", len(self.observations), "Loss:", np.mean(self.loss), "reward:",
              self.reward, "avg reward:", avg_reward, "prob random:", self.probability_of_random_action,
              "unit action:",  self.last_action)

        self.first = False

        if self.step % 100 == 0:
            self.e -= 0.1


        # update old values
        self.last_state = self.current_state
        self.last_action = self.get_action()
        self.reward = 0

        # update probability of random action
        if(self.probability_of_random_action > FINAL_RANDOM_ACTION_PROB and
                   len(self.observations) > OBSERVATION_STEPS):
            self.probability_of_random_action -= (INITIAL_RANDOM_ACTION_PROB - FINAL_RANDOM_ACTION_PROB)/EXPLORE_STEPS



        self.assign_action(self.last_action, 0, units)
        self.terminal = False

    def train(self):
        #episode_history = np.array(self.episode_history)
        #episode_history[:, 1] = discount_rewards(episode_history[:, 1])
        #print(episode_history[:, 1])

        mini_batch = random.sample(self.observations, MINI_BATCH_SIZE)

        previous_states = [ d[0] for d in mini_batch]
        actions = [ d[1] for d in mini_batch]
        rewards = [ d[2] for d in mini_batch]
        current_states = [ d[3] for d in mini_batch]

        agents_expected_reward = []

        feed_dict={
            self.combat_model.state_in: current_states
        }

        agents_reward_per_action = self.sess.run(self.combat_model.unit_1_chosen_action, feed_dict=feed_dict)[0]

        for i in range(len(mini_batch)):
            if mini_batch[i][3]:
                # if this was a terminal step. There is no future reward.
                agents_expected_reward.append(rewards[i])
            else:
                agents_expected_reward.append(
                    rewards[i] + FUTURE_REWARD_DISCOUNT * np.max(agents_reward_per_action[i])
                )

        # learn that these actions in these states lead to this reward

        feed_dict = {
            self.combat_model.state_in: previous_states,
            self.combat_model.unit_1_action: actions,
            self.combat_model.target: agents_expected_reward
        }

        _, self.loss = self.sess.run([self.combat_model.update, self.combat_model.loss], feed_dict=feed_dict)






    def get_action(self):

        new_action = np.zeros([NUM_ACTIONS])

        if np.random.rand(1) <= self.probability_of_random_action:
            action_index = np.random.randint(NUM_ACTIONS)
        else:
            readout_t = self.sess.run(
                self.combat_model.unit_1_output,
                feed_dict={
                    self.combat_model.state_in: [self.current_state]
                })[0]
            action_index = np.argmax(readout_t)

        new_action[action_index] = 1

        return new_action

    def assign_action(self, action, unit_idx, units):

        action = np.argmax(action)

        for unit in units:
            if action == 0:
                unit.attack()

            elif action == 1:
                if unit.unit_class is UnitClass.alchemist:
                    unit.use_bomb_1()

                elif callable(getattr(unit, "spell_1", None)):
                    unit.spell_1()

            elif action == 2:
                if callable(getattr(unit, "bomb_2", None)):
                    unit.bomb_2()

                elif callable(getattr(unit, "spell_2", None)):
                    unit.spell_2()

            elif action == 3:
                if callable(getattr(unit, "bomb_3", None)):
                    unit.bomb_3()

                elif callable(getattr(unit, "spell_3", None)):
                    unit.spell_3()

            elif action == 4:
                if unit.unit_class is UnitClass.knight:
                    unit.taunt()

                elif unit.unit_class is UnitClass.brawler:
                    unit.fit_of_rage()

                elif unit.unit_class is UnitClass.pikeman:
                    unit.target_weakness()

                elif unit.unit_class is UnitClass.magus:
                    unit.elemental_burst()

                elif unit.unit_class is UnitClass.alchemist:
                    # TODO: figure out how to add this later as it requires parameters
                    # unit.special_ability()
                    pass

                elif unit.unit_class is UnitClass.wizard:
                    # TODO: figure out how to add this later as it requires parameters
                    # unit.special_ability()
                    pass

                elif unit.unit_class is UnitClass.sorcerer:
                    # TODO: figure out how to add this later as it requires parameters
                    u.resupply(2)


    def game_over(self):
        print("*****GAME OVER******")


    ##################
    # Helper Methods #
    ##################
    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


