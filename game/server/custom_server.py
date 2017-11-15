from game.server.server_control import ServerControl
from game.utils.generate_game import load
from game.common.node_types import *
from game.common.enums import *
from game.common.unit_classes import get_unit, load_unit
from game.server.combat import CombatManager
from game.common.town_store_options import *
from game.common.item_types import get_item


class CustomServer(ServerControl):

    def __init__(self, verbose=False):
        super().__init__(verbose)

        self.verbose = verbose
        if self.verbose:
            print("Loading Game Data...")
        self.game_map = load()
        if self.verbose:
            print("Game Data Loaded")

        self.current_location = self.game_map.pop(0)[0]

        self.trophies = 0
        self.towns = 0
        self.gold = 300

        self.started = False

        self.combat_manager = None
        self.units = []


    def pre_turn(self):
        self.print("#"*70)
        self.print("SERVER PRE TURN")

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

            elif isinstance(self.current_location, MonsterRoom):
                self.print("Combat against {}".format(self.current_location.monster.get_description()))


                if self.combat_manager is None:
                    self.print("Init new combat manager")
                    self.combat_manager = CombatManager(self.current_location.monster, self.units)


            elif isinstance(self.current_location, TrapRoom):
                self.print("Navgating trap {}".format(self.current_location.trap.get_description()))


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

                #TODO remove this
                if  isinstance(self.current_location, TrapRoom):
                    self.print("Skip TrapRoom")
                    self.current_location.resolved = True

                # HANDLE ROOM NOT RESOLVED
                if not self.current_location.resolved:

                    self.print("Location: {} not resolved.".format(self.current_location))

                    if isinstance(self.current_location, Town):
                        self.print("Notify Player they are in town Town")

                        self.handle_town_purchases()

                        # handle purchases
                        self.current_location.resolved = True



                    elif isinstance(self.current_location, MonsterRoom) and data["message_type"] == MessageType.combat_round:
                        self.print("Combat against {}".format(self.current_location.monster.get_description()))
                        self.print("Do combat with for user.")


                        self.print("Valid data, running combat round.")
                        self.combat_manager.units = data["units"]
                        self.combat_manager.play_round()

                        if self.combat_manager.done:
                            if self.combat_manager.success is True:
                                print("Combat Resolved!")
                                self.trophies += 1
                                self.current_location.resolved = True
                                self.combat_manager = None
                                return
                            elif self.combat_manager.success is False:
                                print("Party Killed! GAME OVER!")
                                print("Trophies Earned: {}".format(self.trophies))
                                self._quit = True # die safely
                                return



                    elif isinstance(self.current_location, TrapRoom):
                        self.print("Navgating trap {}".format(self.current_location.trap.get_description()))

                # HANDLE ROOM RESOLVED
                if self.current_location.resolved:
                    if data["message_type"] == MessageType.room_choice:

                        if len(self.current_location.nodes) == 1 and data["choice"] == Direction.forward:
                            self.current_location = self.current_location.nodes[0]
                            # TODO: LOG location change
                            self.check_end()

                        elif len(self.current_location.nodes) == 2:
                            if data["choice"] == Direction.left:
                                self.current_location = self.current_location.nodes[0]
                                # TODO: LOG location change
                                self.check_end()

                            elif data["choice"] == Direction.right:
                                self.current_location = self.current_location.nodes[1]
                                # TODO: LOG location change
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
                        "message_type":  MessageType.unit_choice
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
                    #payload[i] = self.generate_room_option_payload(self.current_location.nodes)

                    payload[i] = self.combat_manager.serialize_combat_state()

            # send turn data to clients
            payload[i]["units"] = self.serialize_units()


        self.send({
            "type": "server_turn_prompt",
            "payload": payload
        })

    def log(self):
        return {
            "client_turn_data": self.client_turn_data
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
        shop_items = list(town_0)

        if self.towns >= 1:
            shop_items += list(town_1)

        if self.towns >= 2:
            shop_items += list(town_2)

        if self.towns >= 3:
            shop_items += list(town_3)

        if self.towns >= 4:
            shop_items += list(town_4)

        if self.towns >= 5:
            shop_items += list(town_5)

        if self.towns >= 6:
            shop_items += list(town_6)

        if self.towns >= 7:
            shop_items += list(town_7)

        if self.towns >= 8:
            shop_items += list(town_8)

        if self.towns >= 9:
            shop_items += list(town_9)

    def get_unit_by_id(self, id):
        for unit in self.units:
            if unit.id == id:
                return unit
        return None

    def handle_town_purchases(self):

        if self.turn_data["message_type"] == MessageType.town:
            print("Buying items:")

            shop_items = self.get_shop_items()

            for purchase in self.turn_data["purchases"]:

                unit = self.get_unit_by_id(purchase["unit"])

                item_type = purchase["item"]
                item_level = purchase["item_level"]
                if "slot" in purchase:
                    item_slot = purchase["slot"]
                else:
                    item_slot = None

                if ( item_type in valid_purchasers
                     and unit.unit_class in valid_purchasers[item_type]
                     and (self.gold - item_data[item_type][item_level]["cost"]) >= 0 ):

                    item_cost = item_data[item_type][item_level]["cost"]

                    item = None


                    if unit.unit_class in [ UnitClass.knight, UnitClass.brawler, UnitClass.pikeman ]:
                        self.gold -= item_data[item_type][item_level]
                        item = get_item(item_type, item_level)
                        unit.primary_weapon = item

                    if unit.unit_class == UnitClass.rogue:
                        if item_slot is None:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.primary_weapon = item
                        elif item_slot == 1:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.bomb_1 = item
                        elif item_slot == 2:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.bomb_2 = item
                        elif item_slot == 3:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.bomb_3 = item

                    elif unit.unit_class == UnitClass.alchemist:
                        if item_slot is None:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.primary_weapon = item
                        elif item_slot == 1:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.bomb_1 = item
                        elif item_slot == 2:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.bomb_2 = item

                    elif unit.unit_class in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ]:
                        if item_slot is None:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.primary_weapon = item
                        elif item_slot == 1:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.spell_1 = item
                        elif item_slot == 2:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.spell_2 = item
                        elif item_slot == 3:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.spell_3 = item
                        elif item_slot == 4:
                            self.gold -= item_cost
                            item = get_item(item_type, item_level)
                            unit.spell_4 = item

                    if item is not None:
                        print("{0} purchased {1}".format(unit.name, item.name))


