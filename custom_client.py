from game.client.user_client import UserClient
from game.common.enums import *



class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """
        pass

    def unit_choice(self, turn_data):
        print("Sending Unit Choices")

        return {
            "message_type": MessageType.unit_choice,
            "units": [
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
        }


    def town(self, units, gold, store):
        print("Gold: {}".format(gold))

        if store.get_town_number() is 0:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase( unit, 2, ItemType.fire_bomb, 1)


    def room_choice(self, turn_data):

        if len(turn_data["options"]) == 1:

            return { "message_type": MessageType.room_choice, "choice": Direction.forward }

        if len(turn_data["options"]) == 2:

            return { "message_type": MessageType.room_choice, "choice": Direction.left }

        else:
            return { "message_type": MessageType.null }

    def combat_round(self, turn_data):
        print("COMBAT!")
        print(turn_data["monster"].summary())
        for u in turn_data["units"]:
            print(u.summary())

        return_data = { "message_type": MessageType.combat_round }

        for u in turn_data["units"]:
            if u.unit_class == UnitClass.alchemist:
                u.use_bomb_2()
            else:
                u.wait()

        return_data["units"] = turn_data["units"]
        return return_data


    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


