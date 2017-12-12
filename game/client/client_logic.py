from game.common.enums import *
from game.common.node_types import get_node
from game.common.unit_classes import get_unit
from game.common.monster_types import get_monster

import sys

class ClientStorefront:
    def __init__(self, turn_data):
        self.items = turn_data["items"]
        self.purchases = []
        self.town_number = turn_data["town_number"]

    def get_town_number(self):
        return self.town_number


    def purchase(self, unit, item_slot, item, item_level):
        self.purchases.append( {
            "unit": unit.id,
            "slot": item_slot,
            "item": ItemType.fire_bomb,
            "item_level": item_level
        } )

    def get_return_data(self):
        return {
            "message_type": MessageType.town,
            "purchases": self.purchases
        }

class ClientLogic:

    def __init__(self, verbose, player_client):
        self._loop = None
        self._socket_client = None
        self.verbose = verbose
        self.player_client = player_client

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

    def turn(self, turn_data):

        if turn_data["message_type"] == MessageType.unit_choice:
            team_name = self.player_client.team_name()
            choices = self.player_client.unit_choice()
            return {
                "message_type": MessageType.unit_choice,
                "team_name": team_name,
                "units": choices
            }

        elif turn_data["message_type"] == MessageType.town:
            units = turn_data["units"]
            gold = turn_data["gold"]
            store = ClientStorefront(turn_data)
            self.player_client.town(units, gold, store)
            return store.get_return_data()

        elif turn_data["message_type"] == MessageType.room_choice:
            units = turn_data["units"]
            options = turn_data["options"]
            direction = self.player_client.room_choice(units, options)
            return { "message_type": MessageType.room_choice, "choice": direction }

        elif turn_data["message_type"] == MessageType.combat_round:
            monster = turn_data["monster"]
            units = turn_data["units"]
            self.player_client.combat_round(monster, units)
            return { "message_type": MessageType.combat_round, "units": units }

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



