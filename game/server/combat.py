

class CombatManager:

    def __init__(self):
        self.round = 1

        self.done = False
        self.done_reason = ""
        self.success = None

        self.monster = None
        self.units = []

    def serialize_combat_state(self, first=False, last=False):
        data = {}

        if first:
            data["message_type"] = MessageType.combat_begin
        elif last:
            data["message_type"] = MessageType.combat_round
        else:
            data["message_type"] = MessageType.combat_end

        data["monster"] = self.monster.to_dict()

        data["units"] = []
        for u in self.units:
            d = u.to_dict()
            data["units"].append(d)

        return data

    def init(self, monster, units):
        self.monster = monster
        self.units = units


    def play_round(self):

        living_units = [ u for u in self.units if u.is_alive() ]

        # pick targets / moves
        monster_target = self.monster.attack(living_units)

        unit_actions = {}

        for u in living_units:
            unit_actions[u] = u.select_combat_action(monster)

        #########################################
        # apply damage to target / execute move
        #########################################

        print("{0} deals {1} damage to {2}".format(
            self.monster.name,
            self.monster.damage,
            self.monster_target.name))
        monster_target.current_health -= self.monster.damage

        if monster_target.current_health < 0:
            monster_target.current_health = 0

        # apply unit damage to monster
        for unit, action in unit_actions.items():
            double_damage = False
            dmg = 0

            # check for double damage
            for damage_type in action.damage_types:
                if damage_type in self.monster.weaknesses:
                    double_damage = True
                    break

            # apply double damage
            if double_damage:
                dmg += action.damage

            # apply normal damage
            dmg += action.damage

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

        if sum( int(u.is_alive()) for u in units ) == 0:
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

