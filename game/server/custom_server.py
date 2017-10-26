from server_control import ServerControl


class CustomServer(ServerControl):

    def __init__(self):
        super().__init__()


    def pre_turn(self):
        pass

    def post_turn(self):

        pass

    def send_turn_data(self):
        # send turn data to clients
        payload = {}
        import random
        for i in self._client_ids:
            payload[i] = { "fake_data": random.random() }

        # send turn data to clients
        self.send({
            "type": "server_turn_prompt",
            "payload": payload
        })

    def log(self):
        return {
            "client_turn_data": self.client_turn_data
        }
