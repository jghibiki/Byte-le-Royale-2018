from game.client.client_logic import ClientLogic
from game.common.enums import *

class CustomClient(ClientLogic):

    def __init__(self, verbose):
        """
            Availiable Properties:

            self.started : a boolean that representing whether the game has started yet.
            self.tick_no : contains the number of ticks that have occured
        """
        super().__init__(verbose)


    def turn(self, turn_data):

        print()
        print("CLIENT TICK: {}".format(self.tick_no))

        if turn_data["message_type"] == MessageType.unit_choice:

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

        elif turn_data["message_type"] == MessageType.town:

            print("Gold: {}".format(turn_data["gold"]))


            return_data = { "message_type": MessageType.town, "purchases": []}

            if turn_data["town_number"] is 0:
                unit = self.get_unit("thomas", turn_data["units"])
                if unit is not None:
                    purchase = {
                        "unit": unit.id,
                        "slot": 2,
                        "item": ItemType.fire_bomb,
                        "item_level": 1
                    }
                    return_data["purchases"].append(purchase)

            return return_data


        elif turn_data["message_type"] == MessageType.room_choice:

            if len(turn_data["options"]) == 1:

                return { "message_type": MessageType.room_choice, "choice": Direction.forward }

            if len(turn_data["options"]) == 2:

                return { "message_type": MessageType.room_choice, "choice": Direction.left }

            else:
                return { "message_type": MessageType.null }

        elif turn_data["message_type"] == MessageType.combat_round:
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

        else:
            return { "message_type": MessageType.null }




    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


