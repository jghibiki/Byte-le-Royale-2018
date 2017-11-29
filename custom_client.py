from game.client.user_client import UserClient
from game.common.enums import *



class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """
        pass

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
                {
                    "name": "Martin",
                    "class": UnitClass.knight
                },
                {
                    "name": "Steve",
                    "class": UnitClass.brawler
                },
                {
                    "name": "Alphonse",
                    "class": UnitClass.pikeman
                },
                {
                    "name": "Thomas",
                    "class": UnitClass.alchemist
                }
            ]


    def town(self, units, gold, store):
        print("Gold: {}".format(gold))

        if store.get_town_number() is 0:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase( unit, 2, ItemType.fire_bomb, 1)


    def room_choice(self, units, options):

        if len(options) == 1:
            return Direction.forward

        elif len(options) == 2:
            return Direction.left

        else:
            return MessageType.null

    def combat_round(self, monster, units):
        print("COMBAT!")
        print(monster.summary())
        for u in units:
            print(u.summary())

        for u in units:
            if u.unit_class == UnitClass.alchemist:
                u.use_bomb_2()
            else:
                u.attack()



    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


