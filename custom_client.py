from game.client.client_logic import ClientLogic
from game.common.message_types import MessageType
from game.common.directions import Direction

class CustomClient(ClientLogic):

    def __init__(self):
        """
            Availiable Properties:

            self.started : a boolean that representing whether the game has started yet.
            self.tick_no : contains the number of ticks that have occured
        """
        super().__init__()


    def turn(self, turn_data):

        print("tick: {}".format(self.tick_no))
        print(turn_data)


        if turn_data["message_type"] == MessageType.room_choice:

            if len(turn_data["options"]) == 1:

                return { "message_type": MessageType.room_choice, "choice": Direction.forward }

            if len(turn_data["options"]) == 2:

                return { "message_type": MessageType.room_choice, "choice": Direction.left }






