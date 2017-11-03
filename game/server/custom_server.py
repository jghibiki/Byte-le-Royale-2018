from game.server.server_control import ServerControl
from game.utils.generate_game import load
from game.common.node_types import *
from game.common.directions import *
from game.common.message_types import *


class CustomServer(ServerControl):

    def __init__(self):
        super().__init__()

        self.game_map = load()
        self.current_location = self.game_map.pop(0)[0]


    def pre_turn(self):
        print(self.current_location)

        if isinstance(self.current_location, Town):
            print("Town")

            #for u in units:
            #    u.reset_health()

        elif isinstance(self.current_location, MonsterRoom):
            print("Combat against {}".format(self.current_location.monster.get_description()))


        elif isinstance(self.current_location, TrapRoom):
            print("Navgating trap {}".format(self.current_location.trap.get_description()))


    def post_turn(self):

        client_id = self._client_ids[0]

        # handle response if we got one
        if self.client_turn_data[client_id] is not None:
            data = self.client_turn_data[client_id]

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
            payload[i] = { }

            self.current_location.resolved = True # force true to move

            if self.current_location.resolved:
                if isinstance(self.current_location, StartRoom):
                    print("Start Room")
                    payload[i] = self.generate_room_option_payload(self.current_location.nodes)

                elif isinstance(self.current_location, Town):
                    print("Town")


                elif isinstance(self.current_location, MonsterRoom):
                    print("Combat against {}".format(self.current_location.monster.get_description()))


                elif isinstance(self.current_location, TrapRoom):
                    print("Trap Room")

            payload[i] = self.generate_room_option_payload(self.current_location.nodes)

        # send turn data to clients
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

    def check_end(self):
        if isinstance(self.current_location, EndRoom):
            print("*" * 69)
            print(("*" * 25) + " End Room Reached! " + ("*" * 25))
            print("*" * 69)
            self._quit = True
