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

        print("tick: {}".format(self.tick_no))
        print(turn_data)

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

        else:
            return { "message_type": MessageType.null }






