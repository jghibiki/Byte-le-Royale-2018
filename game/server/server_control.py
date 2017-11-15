import random
import os
import json
from datetime import datetime, timedelta


class ServerControl:

    def __init__(self, verbose):

        self._loop = None
        self._socket_client = None
        self.verbose = verbose

        self._clients_connected = 0
        self._client_ids = []
        self._quit = False


        # Game Configuration options
        self.turn_time = 0.01
        self.game_tick_no = 0
        self.max_game_tick = 10 #1e5
        self.turn_data = None

    def initialize(self):
        if self.verbose:
            print("Initializing Server Logic")
        self.send({ "type": "game_starting"})
        self.schedule(self.pre_tick, delay=0.1)

    def wait_for_clients(self):
        if self.verbose:
            print("Waiting for clients...")

        if self._clients_connected < 1:
            self.schedule(self.wait_for_clients, 2)
        else:
            self.schedule(self.initialize, delay=0.1)

    def notify_client_connect(self, client_id):
        self._clients_connected += 1
        self._client_ids.append(client_id)
        self.turn_data = None

    def notify_client_turn(self, turn_data):
        self.turn_data = turn_data

    def pre_tick(self):
        if self.verbose: print("SERVER TICK: {}".format(self.game_tick_no))
        self.game_tick_no += 1

        self.turn_data = None

        self.pre_turn()

        self.send_turn_data()

        self.schedule(self.post_tick)


    def post_tick(self):

        self.post_turn()

        log_data = self.log()
        self.dump_log(log_data)

        if self.game_tick_no < self.max_game_tick and not self._quit:
            self.schedule(self.pre_tick)
        else:
            if self.verbose:
                print("Game Completed")
            self._socket_client.close()
            self.schedule(exit, 3)

    def send_turn_data(self):
        pass

    def set_loop(self, loop):
        self._loop = loop

    def set_socket_client(self, socket_client):
        self._socket_client = socket_client

    def send(self, data):
        self._socket_client.sendAll( data )


    def schedule(self, callback, delay=None):
        self._loop.call_later(
                delay if delay != None else self.turn_time,
                callback)


    def pre_turn(self):
        """ Override. Logic to be executed before the players are allowed to take a turn """
        pass


    def post_turn(self):
        """Override. Logic to be executed after the players have sent turn actions"""
        pass

    def log(self):
        """Override. Dumps state to a file """
        return {}


    def dump_log(self, data):
        if not os.path.exists("game_log"):
            os.makedirs("game_log")

        with open("game_log/{0:05d}.json".format(self.game_tick_no), "w") as f:
            json.dump(data, f)






