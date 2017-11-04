from game.server.server_control import ServerControl
from game.utils.generate_game import load
from game.common.node_types import *
from game.common.enums import *
from game.common.unit_classes import get_unit


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

        self.started = False

        self.combat_manager = None
        self.units = []


    def pre_turn(self):
        print(self.current_location)

        if not self.started:
            # first turn, ask for what units the team should be made up of
            return # purposefully short circuit to get to send data

        if isinstance(self.current_location, Town):
            self.print("Town")

            #for u in units:
            #    u.reset_health()

        elif isinstance(self.current_location, MonsterRoom):
            self.print("Combat against {}".format(self.current_location.monster.get_description()))


        elif isinstance(self.current_location, TrapRoom):
            self.print("Navgating trap {}".format(self.current_location.trap.get_description()))


    def post_turn(self):

        client_id = self._client_ids[0]

        # handle response if we got one
        if client_id in self.client_turn_data and self.client_turn_data[client_id] is not None:
            data = self.client_turn_data[client_id]

            if "message_type" not in data:
                return # bad turn

            if not self.started:
                if data["message_type"] == MessageType.unit_choice:
                    self.units = []

                    # validate unit classes
                    classes = [ u["class"] for u in data["units"] ]
                    unique_classes = list(set(classes))

                    if len(classes) > 4:
                        if self.verbose:
                            print("Too many units defined")
                        return

                    if len(classes) > len(unique_classes):
                        if self.verbose:
                            print("Only one unit of each class allowed.")
                        return

                    for u in  data["units"]:
                        new_unit = get_unit(u["class"], u["name"])
                        self.units.append(new_unit)

                    if self.verbose:
                        print("Client Successfully Sent Desired Unit Types")
                        for u in self.units:
                            print(u)
                    self.started = True

            else:

                self.current_location.resolved = True #TODO remove and implement resolution of types properly
                if self.current_location.resolved and data["message_type"] == MessageType.room_choice:

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

            self.client_turn_data[client_id] = None




    def send_turn_data(self):
        # send turn data to clients
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
                    self.print("Combat against {}".format(self.current_location.monster.get_description()))
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)


                elif isinstance(self.current_location, TrapRoom):
                    self.print("Trap Room")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

        # send turn data to clients
        payload["units"] = self.serialize_units()

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


    def check_end(self):
        if isinstance(self.current_location, EndRoom):
            print("*" * 69)
            print(("*" * 25) + " End Room Reached! " + ("*" * 25))
            print("*" * 69)
            self._quit = True

    def print(self, msg):
        if self.verbose:
            print(msg)


