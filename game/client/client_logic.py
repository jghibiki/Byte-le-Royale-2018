from game.common.message_types import MessageType
from game.common.node_types import *

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

        turn_data = self.deserialize(turn_data)

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

    def deserialize(self, turn_data):

        if turn_data["message_type"] == MessageType.room_choice:
            for direction, room in turn_data["options"].items():
               new_room = get_node(room["node_type"])
               new_room.from_dict(room)
               turn_data["options"][direction] = new_room

        return turn_data

    def serialize(self, turn_result):
        return turn_result



