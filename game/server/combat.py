import math

from game.common.enums import *

class CombatManager:

    def __init__(self, monster, units):
        self.round = 1

        self.monster = monster
        self.units = units

        self.done = False
        self.done_reason = ""
        self.success = None


    def serialize_combat_state(self, first=False, last=False):
        data = {}

        if first:
            data["message_type"] = MessageType.combat_begin
        elif last:
            data["message_type"] = MessageType.combat_end
        else:
            data["message_type"] = MessageType.combat_round

        data["monster"] = self.monster.to_dict()

        data["units"] = []
        for u in self.units:
            d = u.to_dict()
            data["units"].append(d)

        return data



    def play_round(self, unit_actions):

        print(self.units)
        living_units = [ u for u in self.units if u.is_alive() ]

        # pick targets / moves
        monster_target = self.monster.attack(living_units)

        #########################################
        # apply damage to target / execute move
        #########################################

        print("{0} deals {1} damage to {2}".format(
            self.monster.name,
            self.monster.damage,
            monster_target.name))
        monster_target.current_health -= self.monster.damage

        if monster_target.current_health < 0:
            monster_target.current_health = 0

        # apply unit damage to monster
        for unit, action in unit_actions:
            dmg = 0
            dmg_multiplier = 1.0

            # check for double damage
            if action == CombatAction.primary_weapon:
                print("{} deals primary weapon damage to monster".format(unit))
                for damage_type in unit.items[0].damage_types:
                    if damage_type in self.monster.weaknesses:
                        dmg_multiplier += 0.25

                # apply normal damage
                dmg += math.floor(unit.items[0].damage * dmg_multiplier)

                print("{0} deals {1} damage to {2}".format(
                    unit.name,
                    dmg,
                    self.monster.name))

                self.monster.current_health -= dmg

                if self.monster.current_health < 0:
                    self.monster.current_health = 0
                    break

        self.round += 1

        if self.monster.current_health <= 0:
            self.done = True
            self.done_reason = "Monster Defeated!"
            self.success = True

        if sum( int(u.is_alive()) for u in self.units ) == 0:
            self.done = True
            self.done_reason = "Party Defeated!\n Game Over!"
            self.success = False


    def print_summary(self):

        print()
        print("Combat Round {}".format(self.round-1))
        print(self.monster.summary())

        print()
        for u in units:
            print(u.summary())

