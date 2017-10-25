from client_logic import ClientLogic

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

        return turn_data




