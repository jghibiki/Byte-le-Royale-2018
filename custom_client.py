import random

from game.client.user_client import UserClient
from game.common.enums import *



class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """

    def team_name(self):
        print("Sending Team Name")

        return "Team Coffee !@#$$%%^&^**()(*&^%$#"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
                {
                    "name": "Martin",
                    "class": UnitClass.wizard
                },
                {
                    "name": "Steve",
                    "class": UnitClass.brawler
                },
                {
                    "name": "Alphonse",
                    "class": UnitClass.rogue
                },
                {
                    "name": "Thomas",
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
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit, ItemType.fire_bomb, 1, item_slot=2)

        elif store.get_town_number() is 1:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.fire_bomb, 2, item_slot=2)
                store.purchase(unit, ItemType.fire_bomb, 2, item_slot=2)

            unit = self.get_unit("martin", units)
            if unit is not None:
                store.purchase(unit, ItemType.sword, 2)

        elif store.get_town_number() is 3:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.fire_bomb, 3, item_slot=2)
                store.purchase(unit, ItemType.fire_bomb, 3, item_slot=2)

            unit = self.get_unit("martin", units)
            if unit is not None:
                store.purchase(unit, ItemType.sword, 3)

        elif store.get_town_number() is 4:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.fire_bomb, 4, item_slot=2)
                store.purchase(unit, ItemType.fire_bomb, 4, item_slot=2)


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


