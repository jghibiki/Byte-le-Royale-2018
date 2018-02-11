from uuid import uuid4
import math
import random

from game.common.game_serializable import Serializable
from game.common.enums import *

class Trap(Serializable):
    def __init__(self):
        self.initialized = False

    def init(self, trap_type, name, level, stat, pass_type, damage_type, damage_interval, damage, required_effort):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.level = level

        self.trap_type = trap_type
        self.stat = stat
        self.pass_type = pass_type
        self.damage_interval = damage_interval
        self.damage = damage * (math.floor(0.5 * level))
        self.damage_type = damage_type
        self.required_effort = required_effort

        if self.pass_type is TrapPassType.group_pass:
            self.current_effort = 0

        elif (self.pass_type is TrapPassType.individual_pass or
              self.pass_type is TrapPassType.group_pass_on_first_success):
            self.current_effort = [ 0, 0, 0, 0]

        self.initialized = True

    def from_dict(self, d):
        """ Load obj from dict that has been deserialized from json """

        self.id = d["id"]
        self.name = d["name"]
        self.level = d["level"]

        self.trap_type = d["trap_type"]
        self.stat = d["stat"]
        self.pass_type = d["pass_type"]
        self.damage_type = d["damage_type"]
        self.damage_interval = d["damage_interval"]
        self.damage = d["damage"]
        self.required_effort = d["required_effort"]
        self.current_effort = d["current_effort"]

        self.initialized = True


    def to_dict(self):
        """ Dump obj data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "trap_type": self.trap_type,
            "stat": self.stat,
            "pass_type": self.pass_type,
            "damage_interval": self.damage_interval,
            "damage_type": self.damage_type,
            "damage": self.damage,
            "required_effort": self.required_effort,
            "current_effort": self.current_effort
        }

    def get_description(self):
        return "{0}".format(self.name)

    def summary(self):

        out = "{0}:".format(self.name).rjust(15)

        if self.pass_type is TrapPassType.group_pass:
            percent_completed = self.current_effort / float(self.required_effort)
            bar_size = 50
            percent_bar = math.floor( bar_size * percent_completed)

            out += " Effort:({0:04d}/{1:04d})[{2}]".format(
                self.current_effort,
                self.required_effort,
                ("="*percent_bar).ljust(bar_size, " "))

        elif(self.pass_type is TrapPassType.group_pass_on_first_success or
             self.pass_type is TrapPassType.individual_pass):

            for i in range(4):
                percent_completed = self.current_effort[i] / float(self.required_effort)
                bar_size = 10
                percent_bar = math.floor( bar_size * percent_completed)

                out += " U{0} Effort({1:04d}/{2:04d})[{3}]".format(
                    i,
                    self.current_effort[i],
                    self.required_effort,
                    ("="*percent_bar).ljust(bar_size, " "))

        return out

