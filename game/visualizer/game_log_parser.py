import json
import os

from game.common.enums import *
from game.common.unit_classes import get_unit, load_unit
from game.common.node_types import get_node

class GameLogParser:
    def __init__(self, log_dir):

        if not os.path.exists(log_dir):
            raise Exception("Invalid log directory: {}".format(log_dir))

        self.log_dir = log_dir

        # parse manifest
        with open("{}/manifest.json".format(log_dir), "r") as f:
            manifest = json.load(f)
            self.max_ticks = manifest["ticks"]

        self.tick = 1


    def get_turn(self):
        with open("{0}/{1:05d}.json".format(self.log_dir, self.tick), "r") as f:
            turn = json.load(f)

        units, events = self._parse_turn(turn)

        return units, events


    def _parse_turn(self, turn):

        units = self._deserialize_units( turn["units"] )
        units = sorted(units, key=lambda u: u.id)

        location = None

        for event in turn["turn_result"]["events"]:

            if event["type"] == Event.unit_health_restored:
                pass # do nothing, just a signal

            elif event["type"] == Event.begin_combat:
                pass # do nothing, just a signal

            elif event["type"] == Event.set_location:
                node = get_node(event["location"]["node_type"])
                node.from_dict(event["location"])

                event["location"] = node


            elif event["type"] == Event.purchase_item:
                pass #do nothing, a signal wit some display data

            elif event["type"] == Event.combat_resolved:
                pass #do nothing, a signal with updates for gold an trophies

            elif event["type"] == Event.party_killed:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.special_ability:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.special_ability_charging:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.special_ability_attack:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.monster_attack:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.unit_attack:
                pass # do nothing, just a signal with some display data

            elif event["type"] == Event.room_choice:

                if event["room_1"] is not None:
                    node = get_node(event["room_1"]["node_type"])
                    node.from_dict(event["room_1"])
                    event["room_1"] = node

                if event["room_2"] is not None:
                    node = get_node(event["room_2"]["node_type"])
                    node.from_dict(event["room_2"])
                    event["room_2"] = node

        return units, turn["turn_result"]["events"]


    def _deserialize_units(self, units):
        deserialized_units = []
        for u in units:
            unit = load_unit(u["unit_class"], u)
            deserialized_units.append(unit)
        return deserialized_units

    def _get_unit(self, unit_id, units):

        for unit in units:
            if unit.id == unit_id:
                return unit
        return None
