from game.common.enums import *
from game.common.node_types import get_node
from game.common.unit_classes import get_unit
from game.common.monster_types import get_monster

import sys

class ClientLogic:

    def __init__(self, verbose):
        self._loop = None
        self._socket_client = None
        self.verbose = verbose

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

        serialized_turn_result = self.serialize(turn_result)

        self.send({
            "type": "client_turn",
            "payload": serialized_turn_result
        })

    def turn(self):
        """ Implement game logic here."""
        pass

    def send(self, data):
        self._socket_client.send(data)

    def notify_game_started(self):
        if self.verbose:
            print("Game Started")
        self.started_game = True

    def deserialize(self, turn_data):

        # load units
        units = []
        if "units" in turn_data:
            for u in turn_data["units"]:
                new_unit = get_unit(u["unit_class"])
                new_unit.from_dict(u)
                units.append(new_unit)

        turn_data["units"] = units

        # load message type specific data
        if turn_data["message_type"] == MessageType.room_choice:
            # deserialize rooms
            for direction, room in turn_data["options"].items():
               new_room = get_node(room["node_type"])
               new_room.from_dict(room)
               turn_data["options"][direction] = new_room

        if turn_data["message_type"] == MessageType.combat_round:
            # deserialize monster
            monster = get_monster(turn_data["monster"]["monster_type"])
            monster.from_dict(turn_data["monster"])
            turn_data["monster"] = monster


        return turn_data

    def serialize(self, turn_result):

        if turn_result["message_type"] == MessageType.combat_round:
            serialized_units = []

            for u in turn_result["units"]:
                serialized_units.append( u.to_dict() )

            turn_result["units"] = serialized_units

        return turn_result



