import random

from game.client.user_client import UserClient
from game.common.enums import *



class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """

    def team_name(self):
        print("Sending Team Name")

        return "Team Longcoats"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
                {
                    "name": "Ed",
                    "class": UnitClass.knight
                },
                {
                    "name": "Edd",
                    "class": UnitClass.brawler
                },
                {
                    "name": "Eddy",
                    "class": UnitClass.pikeman
                },
                {
                    "name": "Carlos",
                    "class": UnitClass.alchemist
                }
            ]


    def town(self, units, gold, store):
        print()
        print("*"*50)
        print("Town")
        print("*"*50)

        print("Gold: {}".format(gold))


        if store.get_town_number() is 0:
            unit1 = self.get_unit("ed", units)
            unit2 = self.get_unit("edd", units)
            unit3 = self.get_unit("eddy", units)
            unit4 = self.get_unit("carlos", units)
            if unit1 is not None:
                store.purchase(unit1, 2, ItemType.sword, 1)
            if unit2 is not None:
                store.purchase(unit2, 2, ItemType.mace, 1)
            if unit3 is not None:
                store.purchase(unit3, 2, ItemType.spear, 1)
            if unit4 is not None:
                store.purchase(unit4, 2, ItemType.fire_bomb, 1)
                store.purchase(unit4, 2, ItemType.fire_bomb, 1)
                
        elif store.get_town_number() is 1:
            unit = self.get_unit("carlos", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 2)
                store.purchase(unit, 2, ItemType.fire_bomb, 2)

        elif store.get_town_number() is 3:
            unit = self.get_unit("carlos", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 3)
                store.purchase(unit, 2, ItemType.fire_bomb, 3)

        elif store.get_town_number() is 4:
            unit = self.get_unit("carlos", units)
            if unit is not None:
                store.purchase(unit, 2, ItemType.fire_bomb, 4)
                store.purchase(unit, 2, ItemType.fire_bomb, 4)


    def room_choice(self, units, options):

        if len(options) == 1:
            return Direction.forward

        elif len(options) == 2:
            return random.choice([Direction.right, Direction.left])
        else:
            return MessageType.null

    def combat_round(self, monster, units):
        print()
        print("*"*50)
        print("Combat")
        print("*"*50)
        print(monster.summary())
        for u in units:
            print(u.summary())

        for u in units:
            if u.unit_class == UnitClass.alchemist:
                if u.bomb_2_quantity > 0:
                    u.use_bomb_2()
                else:
                    u.resupply(2)
            elif u.unit_class == UnitClass.knight:
                    if monster.health > 1000 and u.health > 1000:
                        u.taunt()
                    else:
                        u.attack()
            else:
                u.attack()

    def trap_round(self, trap, units):
        print()
        print("*"*50)
        print("Trap!")
        print("*"*50)
        print(trap.summary())
        for u in units:
            print(u.summary())

        for u in units:
            u.trap_action = random.choice([TrapAction.little_effort, TrapAction.large_effort, TrapAction.evade])


    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


