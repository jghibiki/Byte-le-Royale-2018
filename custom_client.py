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
                        "name": "Ed",
                        "class": UnitClass.pikeman
                    },
                    {
                        "name": "Thomas",
                        "class": UnitClass.rogue
                    }
                ]
            }


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
                if u.unit_class == UnitClass.pikeman:
                    u.target_weakness()
                else:
                    u.wait()

            return_data["units"] = turn_data["units"]
            return return_data

        else:
            return { "message_type": MessageType.null }





