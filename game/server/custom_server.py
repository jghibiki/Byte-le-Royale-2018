from game.server.server_control import ServerControl
from game.utils.generate_game import load
from game.common.node_types import *
from game.common.enums import *
from game.common.unit_classes import get_unit
from game.server.combat import CombatManager


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
        self.print("#"*70)
        self.print("SERVER PRE TURN")

        if not self.started:
            # first turn, ask for what units the team should be made up of
            return # purposefully short circuit to get to send data

        if isinstance(self.current_location, Town):
            self.print("Town")

            #for u in units:
            #    u.reset_health()

        elif isinstance(self.current_location, MonsterRoom):
            self.print("Combat against {}".format(self.current_location.monster.get_description()))


            if self.combat_manager is None:
                self.print("Init new combat manager")
                self.combat_manager = CombatManager(self.current_location.monster, self.units)


        elif isinstance(self.current_location, TrapRoom):
            self.print("Navgating trap {}".format(self.current_location.trap.get_description()))


    def post_turn(self):
        self.print("SERVER POST TURN")

        client_id = self._client_ids[0]

        # handle response if we got one
        if client_id in self.client_turn_data and self.client_turn_data[client_id] is not None:
            data = self.client_turn_data[client_id]
            print(data)

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
                if isinstance(self.current_location, Town) or isinstance(self.current_location, TrapRoom):
                    self.print("Skip Town or TrapRoom")
                    self.current_location.resolved = True

                # HANDLE ROOM NOT RESOLVED
                if not self.current_location.resolved:

                    self.print("Location: {} not resolved.".format(self.current_location))

                    if isinstance(self.current_location, Town):
                        self.print("Notify Player they are in town Town")

                        #for u in units:
                        #    u.reset_health()

                    elif isinstance(self.current_location, MonsterRoom) and data["message_type"] == MessageType.combat_round:
                        self.print("Combat against {}".format(self.current_location.monster.get_description()))
                        self.print("Do combat with for user.")

                        if "actions" in data:
                            actions = []
                            for name, action in data["actions"].items():
                                for unit in self.units:
                                    if name == unit.name:
                                        actions.append( [ unit, action ] )
                                        break
                                    

                            self.print("Valid data, running combat round.")
                            self.combat_manager.play_round(actions)

                            if self.combat_manager.done:
                                if self.combat_manager.success is True:
                                    print("Combat Resolved!")
                                    self.current_location.resolved = True
                                    self.combat_manager = None
                                    return 
                                elif self.combat_manager.success is False:
                                    print("Party Killed! GAME OVER!")
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

		

            self.client_turn_data[client_id] = None




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
                    self.print("Town")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)


                elif isinstance(self.current_location, TrapRoom):
                    self.print("Trap Room")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

            elif not self.current_location.resolved:

                if isinstance(self.current_location, MonsterRoom):
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


    def check_end(self):
        if isinstance(self.current_location, EndRoom):
            print("*" * 69)
            print(("*" * 25) + " End Room Reached! " + ("*" * 25))
            print("*" * 69)
            self._quit = True

    def print(self, msg):
        if self.verbose:
            print(msg)


