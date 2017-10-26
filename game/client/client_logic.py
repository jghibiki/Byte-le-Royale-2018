

class ClientLogic:

    def __init__(self):
        self._loop = None
        self._socket_client = None

        # Public properties availiable to users

        self.started_game = False
        self.tick_no = 0

    def set_loop(self, loop):
        self._loop = loop

    def set_socket_client(self, socket_client):
        self._socket_client = socket_client

    def initialize(self):

        self.send({
            "type": "register"
        })

    def tick(self, turn_data):
        self.tick_no += 1
        turn_result = self.turn(turn_data)

        self.send({
            "type": "client_turn",
            "payload":turn_result
        })

    def turn(self):
        """ Implement game logic here."""
        pass

    def send(self, data):
        self._socket_client.send(data)

    def notify_game_started(self):
        print("Game Started")
        self.started_game = True


