import json

from game.server.server_control import ServerControl
from game.utils.generate_game import load
from game.common.node_types import *
from game.common.enums import *
from game.common.unit_classes import get_unit, load_unit
from game.server.combat_manager import CombatManager
from game.server.trap_manager import TrapManager
from game.common.town_store_options import *
from game.common.item_types import get_item


class CustomServer(ServerControl):

    def __init__(self, verbose=False, server_loop=False, wait_on_client=False):
        super().__init__(wait_on_client, verbose)

        self.verbose = verbose
        self.server_loop = server_loop

        if self.verbose:
            print("Loading Game Data...")
        self.game_map = load()
        if self.verbose:
            print("Game Data Loaded")

        self.current_location = self.game_map.pop(0)[0]

        self.trophies = 0
        self.towns = 0
        self.gold = 2000
        self.total_gold = 2000

        self.max_combat_rounds = 1000

        self.started = False

        self.combat_manager = None
        self.trap_manager = None
        self.units = []
        self.team_name = "[No team name set]"

        self.turn_log = None

    def reinit(self):
        if self.verbose:
            print("*******Restarting*****")

        self.game_map = load()
        if self.verbose:
            print("Game Data Loaded")

        self.current_location = self.game_map.pop(0)[0]

        self.trophies = 0
        self.towns = 0
        self.gold = 2000
        self.total_gold = 2000

        self.started = False

        self.combat_manager = None
        self.trap_manager = None
        self.units = []
        self.team_name = "[No team name set]"

    def pre_turn(self):
        self.print("#"*70)
        self.print("SERVER PRE TURN")

        # reset turn result
        self.turn_log = { "events":[
            {
                "type": Event.set_location,
                "location": self.current_location.to_dict()
            }
        ],
            "team_name": self.team_name
        }

        if not self.started:
            # first turn, ask for what units the team should be made up of
            return # purposefully short circuit to get to send data

        if not self.current_location.resolved:
            if isinstance(self.current_location, Town):
                self.print("Town")

                print("Welcome to town.")
                print("Your entire party spends a night in an inn and wakes feeling refreshed.")
                for u in self.units:
                    u.reset_health()

                self.turn_log["events"].append({"type":Event.unit_health_restored})

            elif isinstance(self.current_location, MonsterRoom):
                self.print("Combat against {}".format(self.current_location.monster.get_description()))

                if self.combat_manager is None:
                    self.print("Init new combat manager")
                    self.combat_manager = CombatManager(self.current_location.monster, self.units, self.verbose)
                    self.turn_log["events"].append({ "type": Event.begin_combat })


            elif isinstance(self.current_location, TrapRoom):
                self.print("Navgating trap {}".format(self.current_location.trap.get_description()))

                if self.trap_manager is None:
                    self.trap_manager = TrapManager(self.current_location.trap, self.units, self.verbose)
                    self.turn_log["events"].append({ "type": Event.begin_trap_evade })


    def post_turn(self):
        self.print("SERVER POST TURN")

        self.deserialize_turn_data()

        # handle response if we got one
        if self.turn_data is not None:
            data = self.turn_data

            if "message_type" not in data:
                return # bad turn

            if not self.started:
                if data["message_type"] == MessageType.unit_choice:
                    self.team_name = data["team_name"]
                    self.units = []

                    # validate unit classes
                    classes = [ u["class"] for u in data["units"] ]
                    unique_classes = list(set(classes))

                    if len(classes) > 4:
                        raise Exception("Too many units defined")

                    if len(classes) > len(unique_classes):
                        raise Exception("Only one unit of each class allowed.")

                    for u in  data["units"]:
                        new_unit = get_unit(u["class"], u["name"])
                        self.units.append(new_unit)

                    if self.verbose:
                        self.print("Client Successfully Sent Desired Unit Types")
                        for u in self.units:
                            self.print(u)

                    self.started = True

            else:

                # HANDLE ROOM NOT RESOLVED
                if not self.current_location.resolved:

                    self.print("Location: {} not resolved.".format(self.current_location))

                    if isinstance(self.current_location, Town):
                        self.print("Notify Player they are in town Town")

                        self.handle_town_purchases()

                        self.towns += 1

                        # handle purchases
                        self.current_location.resolved = True


                    elif isinstance(self.current_location, MonsterRoom) and data["message_type"] == MessageType.combat_round:
                        self.print("Combat against {}".format(self.current_location.monster.get_description()))
                        self.print("Do combat with for user.")


                        self.print("Valid data, running combat round.")
                        self.combat_manager.units = data["units"]
                        self.combat_manager.play_round(self.turn_log)

                        if self.combat_manager.done:


                            if self.combat_manager.success is True:
                                print("Combat Resolved!")
                                self.trophies += 1
                                self.gold += self.current_location.monster.gold
                                self.total_gold += self.current_location.monster.gold

                                self.turn_log["events"].append({
                                    "type": Event.combat_resolved,
                                    "trophies": self.trophies,
                                    "gold": self.gold
                                })

                                self.current_location.resolved = True
                                self.combat_manager = None
                                return
                            elif self.combat_manager.success is False:
                                self.game_over()
                            elif self.combat_manager.round >= self.max_combat_rounds:
                                print("Max Combat Rounds Reached: {}. Exiting. Intentional turtling possible.".format(self.combat_manager.round))
                                self.game_over()

                    elif isinstance(self.current_location, TrapRoom):
                        self.print("Navgating trap {}".format(self.current_location.trap.get_description()))

                        self.trap_manager.units = data["units"]
                        self.trap_manager.play_round(self.turn_log)

                        if self.trap_manager.done:

                            if self.trap_manager.success is True:

                                self.turn_log["events"].append({
                                    "type": Event.trap_resolved,
                                })

                                for unit in self.units:
                                    unit.current_focus = unit.focus
                                    unit.current_will = unit.will

                                self.trap_manager = None
                                self.current_location.resolved = True

                            else:
                                self.game_over()

                # HANDLE ROOM RESOLVED
                if self.current_location.resolved:
                    if data["message_type"] == MessageType.room_choice:

                        if len(self.current_location.nodes) == 1 and data["choice"] == Direction.forward:

                            self.turn_log["events"].append({
                                "type": Event.room_choice,
                                "room_1": self.current_location.nodes[0].to_dict(),
                                "room_2": None,
                                "choice": "room_1"
                            })

                            self.current_location = self.current_location.nodes[0]
                            self.check_end()


                        elif len(self.current_location.nodes) == 2:
                            if data["choice"] == Direction.left:

                                self.turn_log["events"].append({
                                    "type": Event.room_choice,
                                    "room_1": self.current_location.nodes[0].to_dict(),
                                    "room_2": self.current_location.nodes[1].to_dict(),
                                    "choice": "room_1"
                                })

                                self.current_location = self.current_location.nodes[0]
                                self.check_end()

                            elif data["choice"] == Direction.right:

                                self.turn_log["events"].append({
                                    "type": Event.room_choice,
                                    "room_1": self.current_location.nodes[0].to_dict(),
                                    "room_2": self.current_location.nodes[1].to_dict(),
                                    "choice": "room_2"
                                })

                                self.current_location = self.current_location.nodes[1]
                                self.check_end()

            self.client_turn_data = None



    def send_turn_data(self):
        # send turn data to clients
        self.print("SERVER SEND DATA")
        payload = {}
        import random
        for i in self._client_ids:
            payload[i] = { "message_type": MessageType.null }

            if not self.started:
                if self.verbose: print("Requesting Unit Choice")
                payload[i] = {
                        "message_type":  MessageType.unit_choice,
                        "units": self.serialize_units()
                }

            elif self.current_location.resolved:
                if isinstance(self.current_location, StartRoom):
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

                elif isinstance(self.current_location, Town):
                    self.print("Town")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

                elif isinstance(self.current_location, MonsterRoom):
                    self.print("Monster Room")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

                elif isinstance(self.current_location, TrapRoom):
                    self.print("Trap Room")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

            elif not self.current_location.resolved:

                if isinstance(self.current_location, Town):
                    payload[i] = self.generate_town_option_payload()

                elif isinstance(self.current_location, MonsterRoom):
                    self.print("Combat against {}".format(self.current_location.monster.get_description()))
                    payload[i] = self.combat_manager.serialize_combat_state()

                elif isinstance(self.current_location, TrapRoom):
                    self.print("Combat against {}".format(self.current_location.trap.get_description()))
                    payload[i] = self.trap_manager.serialize_state()

            # send turn data to clients
            payload[i]["units"] = self.serialize_units()


        self.send({
            "type": "server_turn_prompt",
            "payload": payload
        })

    def log(self):
        return {
            "turn_result": self.turn_log,
            "units": self.serialize_units()
        }


    def generate_room_option_payload(self, rooms):
        if len(rooms) == 1:
            return {
                "message_type": MessageType.room_choice,
                "options": { Direction.forward: rooms[0].to_dict() }
            }

        elif len(rooms) == 2:
            return {
                "message_type": MessageType.room_choice,
                "options": {
                    Direction.left: rooms[0].to_dict(),
                    Direction.right: rooms[1].to_dict()
                }
            }

    def serialize_units(self):
        units = []
        for u in self.units:
            units.append( u.to_dict() )

        return units

    def deserialize_units(self, units):
        deserialized_units = []
        for u in self.turn_data["units"]:
            unit = load_unit(u["unit_class"], u)
            deserialized_units.append(unit)
        return deserialized_units


    def deserialize_turn_data(self):

        if self.turn_data is not None:
            if self.turn_data["message_type"] != MessageType.unit_choice:
                if "units" in self.turn_data:
                    self.turn_data["units"] = self.deserialize_units(self.turn_data["units"])
                    self.units = self.turn_data["units"]


    def check_end(self):
        if isinstance(self.current_location, EndRoom):
            print("*" * 69)
            print(("*" * 25) + " End Room Reached! " + ("*" * 25))
            print("*" * 69)
            self._quit = True

    def print(self, msg):
        if self.verbose:
            print(msg)


    def generate_town_option_payload(self):

        payload = {
            "message_type": MessageType.town,
            "gold": self.gold,
            "town_number": self.towns,
            "units": self.serialize_units()
        }

        payload["items"] = self.get_shop_items()

        return payload

    def get_shop_items(self):
        shop_items = list(towns[0])

        if self.towns >= 1:
            shop_items += list(towns[1])

        if self.towns >= 2:
            shop_items += list(towns[2])

        if self.towns >= 3:
            shop_items += list(towns[3])

        if self.towns >= 4:
            shop_items += list(towns[4])

        if self.towns >= 5:
            shop_items += list(towns[5])

        if self.towns >= 6:
            shop_items += list(towns[6])

        if self.towns >= 7:
            shop_items += list(towns[7])

        if self.towns >= 8:
            shop_items += list(towns[8])

        if self.towns >= 9:
            shop_items += list(towns[9])

        return shop_items

    def get_unit_by_id(self, id):
        for unit in self.units:
            if unit.id == id:
                return unit
        return None

    def game_over(self):

        print()
        print("*"*50)
        print("Party Killed! GAME OVER!")
        print("Trophies Earned: {}".format(self.trophies))
        print("Current Gold: {}".format(self.gold))
        print("Total Gold: {}".format(self.total_gold))
        print("Levels Cleared: {}".format(self.towns-1))
        print("*"*50)


        self.turn_log["events"].append({
            "type": Event.party_killed,
            "trophies": self.trophies,
            "gold": self.gold,
            "total_gold": self.total_gold,
            "levels_cleared": self.towns-1
        })

        unit_loadouts = []

        for unit in self.units:
            unit_data = {}

            if unit.unit_class == UnitClass.knight:
                unit_data["class"] = "Knight"
            elif unit.unit_class == UnitClass.pikeman:
                unit_data["class"] = "Pikeman"
            elif unit.unit_class == UnitClass.brawler:
                unit_data["class"] = "Brawler"
            elif unit.unit_class == UnitClass.rogue:
                unit_data["class"] = "Rogue"
            elif unit.unit_class == UnitClass.magus:
                unit_data["class"] = "Magus"
            elif unit.unit_class == UnitClass.wizard:
                unit_data["class"] = "Wizard"
            elif unit.unit_class == UnitClass.sorcerer:
                unit_data["class"] = "Sorcerer"
            elif unit.unit_class == UnitClass.alchemist:
                unit_data["class"] = "Alchemist"

            unit_data["primary_name"] = unit.primary_weapon.name
            unit_data["primary_level"] = unit.primary_weapon.level

            if unit.armor is not None:
                unit_data["armor_level"] = unit.armor.level
            else:
                unit_data["armor_level"] = None

            if unit.unit_class in [UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer]:
                if unit.spell_1 is not None:
                    unit_data["spell_1_name"] = unit.spell_1.name
                    unit_data["spell_1_level"] = unit.spell_1.level

                if unit.spell_2 is not None:
                    unit_data["spell_2_name"] = unit.spell_2.name
                    unit_data["spell_2_level"] = unit.spell_2.level

                if unit.spell_3 is not None:
                    unit_data["spell_3_name"] = unit.spell_3.name
                    unit_data["spell_3_level"] = unit.spell_3.level

            elif unit.unit_class == UnitClass.rogue:
                if unit.bomb_1 is not None:
                    unit_data["bomb_1_name"] = unit.bomb_1.name
                    unit_data["bomb_1_level"] = unit.bomb_1.level

                if unit.bomb_2 is not None:
                    unit_data["bomb_2_name"] = unit.bomb_2.name
                    unit_data["bomb_2_level"] = unit.bomb_2.level

                if unit.bomb_3 is not None:
                    unit_data["bomb_3_name"] = unit.bomb_3.name
                    unit_data["bomb_3_level"] = unit.bomb_3.level

            elif unit.unit_class == UnitClass.alchemist:
                if unit.bomb_1 is not None:
                    unit_data["bomb_1_name"] = unit.bomb_1.name
                    unit_data["bomb_1_level"] = unit.bomb_1.level

                if unit.bomb_2 is not None:
                    unit_data["bomb_2_name"] = unit.bomb_2.name
                    unit_data["bomb_2_level"] = unit.bomb_2.level

            unit_loadouts.append(unit_data)



        with open("result.json", "w") as f:
            json.dump({
                "trophies": self.trophies,
                "gold": self.gold,
                "total_gold": self.total_gold,
                "levels_cleared": self.towns-1,
                "unit_loadouts": unit_loadouts
            }, f)

        if self.server_loop:
            self.notify_game_over()
            self.reinit()
        else:
            self._quit = True # die safely
        return

    def handle_town_purchases(self):

        if self.turn_data["message_type"] == MessageType.town:
            print("Buying items:")

            shop_items = self.get_shop_items()

            for purchase in self.turn_data["purchases"]:

                unit = self.get_unit_by_id(purchase["unit"])

                item_type = purchase["item"]
                item_level = purchase["item_level"]

                if level > 10:
                    continue

                avail = any(True for item in shop_items
                            if item["type"] == item_type and item["level"] == item_level )

                if not avail:
                    continue

                if "slot" in purchase:
                    item_slot = purchase["slot"]
                else:
                    item_slot = None

                if ( item_type in valid_purchasers
                     and unit.unit_class in valid_purchasers[item_type]
                     and (self.gold - item_data[item_type][item_level]["cost"]) >= 0 ):


                    item_cost = item_data[item_type][item_level]["cost"]

                    item = None

                    if item_type is ItemType.armor:
                        self.gold -= item_cost
                        item = get_item(item_type, item_level, unit_class=unit.unit_class)
                        unit.armor = item
                        unit.current_health = item.health
                        unit.health = item.health

                        self.turn_log["events"].append({
                            "type": Event.purchase_item,
                            "gold": self.gold,
                            "unit": unit.id,
                            "slot": ItemSlot.armor
                        })
                    else:

                        if unit.unit_class in [ UnitClass.knight, UnitClass.brawler, UnitClass.pikeman ]:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.primary_weapon = item

                            self.turn_log["events"].append({
                                "type": Event.purchase_item,
                                "gold": self.gold,
                                "unit": unit.id,
                                "slot": ItemSlot.primary
                            })

                        if unit.unit_class == UnitClass.rogue:

                            if item_slot is None:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.primary_weapon = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.primary
                                })

                            elif item_slot == 1:
                                self.gold -= item_cost

                                if(unit.bomb_1 is not None and
                                   item_type is unit.bomb_1.item_type and
                                   item_level is unit.bomb_1.level and
                                   unit.bomb_1_quantity < 2):
                                        unit.bomb_1_quantity += 1
                                else:
                                    item = get_item(item_type, item_level)
                                    unit.bomb_1 = item
                                    unit.bomb_1_quantity = 1

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.bomb_1
                                })

                            elif item_slot == 2:

                                self.gold -= item_cost

                                if(unit.bomb_2 is not None and
                                   item_type is unit.bomb_2.item_type and
                                   item_level is unit.bomb_2.level and
                                   unit.bomb_2_quantity < 2):
                                    unit.bomb_2_quantity += 1
                                else:
                                    item = get_item(item_type, item_level)
                                    unit.bomb_2 = item
                                    unit.bomb_2_quantity = 1

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.bomb_2
                                })

                            elif item_slot == 3:
                                self.gold -= item_cost

                                if(unit.bomb_3 is not None and
                                   item_type is unit.bomb_3.item_type and
                                   item_level is unit.bomb_3.level and
                                   unit.bomb_3_quantity < 2):
                                    unit.bomb_3_quantity += 1
                                else:
                                    item = get_item(item_type, item_level)
                                    unit.bomb_3 = item
                                    unit.bomb_3_quantity = 1

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.bomb_3
                                })


                        elif unit.unit_class == UnitClass.alchemist:
                            if item_slot is None:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.primary_weapon = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.primary
                                })

                            elif item_slot == 1:
                                self.gold -= item_cost

                                if(unit.bomb_1 is not None and
                                   item_type is unit.bomb_1.item_type and
                                   item_level is unit.bomb_1.level and
                                   unit.bomb_1_quantity < 2):
                                    unit.bomb_1_quantity += 1
                                else:
                                    item = get_item(item_type, item_level)
                                    unit.bomb_1 = item
                                    unit.bomb_1_quantity = 1

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.bomb_1
                                })

                            elif item_slot == 2:
                                self.gold -= item_cost

                                if(unit.bomb_2 is not None and
                                   item_type is unit.bomb_2.item_type and
                                   item_level is unit.bomb_2.level and
                                   unit.bomb_2_quantity < 2):

                                    unit.bomb_2_quantity += 1
                                else:
                                    item = get_item(item_type, item_level)
                                    unit.bomb_2 = item
                                    unit.bomb_2_quantity = 1

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.bomb_2
                                })

                        elif unit.unit_class in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ]:
                            if item_slot is None:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.primary_weapon = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.primary
                                })

                            elif item_slot == 1:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.spell_1 = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.spell_1
                                })

                            elif item_slot == 2:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.spell_2 = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.spell_2
                                })

                            elif item_slot == 3:
                                self.gold -= item_cost
                                item = get_item(item_type, item_level)
                                unit.spell_3 = item

                                self.turn_log["events"].append({
                                    "type": Event.purchase_item,
                                    "gold": self.gold,
                                    "unit": unit.id,
                                    "slot": ItemSlot.spell_3
                                })


                    if item is not None:
                        print("{0} purchased {1}".format(unit.name, item.name))


