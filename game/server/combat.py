

class CombatManager:

    def __init__(self):
        self.round = 1

        self.done = False
        self.done_reason = ""
        self.success = None

    def play_round(self, monster, units):


        living_units = [ u for u in units if u.is_alive() ]


        # pick targets / moves
        monster_target = monster.attack(living_units)

        unit_actions = {}

        for u in living_units:
            unit_actions[u] = u.select_combat_action(monster)

        #########################################
        # apply damage to target / execute move
        #########################################

        # calculate monster damage
        dmg = monster.damage - monster_target.defense

        # apply monster damage if positive
        if dmg > 0:
            print("{0} deals {1} damage to {2}".format(monster.name, dmg, monster_target.name))
            monster_target.current_health -= dmg

            if monster_target.current_health < 0:
                monster_target.current_health = 0

        # apply unit damage to monster
        for unit, action in unit_actions.items():
            double_damage = False
            dmg = 0

            # check for double damage
            for damage_type in action.damage_types():
                if damage_type in monster.weaknesses:
                    double_damage = True
                    break

            # apply double damage
            if double_damage:
                dmg += (action.damage - monster.defense)

            # apply normal damage
            dmg += (action.damage - monster.defense)

            if dmg > 0:
                print("{0} deals {1} damage to {2}".format(unit.name, dmg, monster.name))
                monster.current_health -= dmg

                if monster.current_health < 0:
                    monster.current_health = 0
                    break

        self.round += 1

        if monster.current_health <= 0:
            self.done = True
            self.done_reason = "Monster Defeated!"
            self.success = True

        if sum( int(u.is_alive()) for u in units ) == 0:
            self.done = True
            self.done_reason = "Party Defeated!\n Game Over!"
            self.success = False

        return monster, units


    def print_summary(self, monster, units):

        print()
        print("Combat Round {}".format(self.round-1))
        print(monster.summary())

        print()
        for u in units:
            print(u.summary())

