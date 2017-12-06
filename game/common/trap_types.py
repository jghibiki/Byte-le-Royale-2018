import random

from game.common.trap import Trap
from game.common.enums import *



def get_trap(trap_type):
    if trap_type == TRAP_TYPE.pit_trap:
        return PitTrap()
    elif trap_type == TRAP_TYPE.spike_trap:
        return SpikeTrap()
    elif trap_type == TRAP_TYPE.boulder_trap:
        return BoulderTrap()
    elif trap_type == TRAP_TYPE.dart_trap:
        return DartTrap()
    elif trap_type == TRAP_TYPE.narrow_bridge:
        return NarrowBridge()

def get_random_trap():
    trap_type = random.choice([
        TRAP_TYPE.pit_trap,
        TRAP_TYPE.spike_trap,
        TRAP_TYPE.boulder_trap,
        TRAP_TYPE.dart_trap,
        TRAP_TYPE.narrow_bridge,
    ])

    return get_trap(trap_type)



class PitTrap(Trap):
    def init(self, level):
        Trap.init(self, "Pit Trap", level)

        self.counters = [

        ]

    def get_type(self):
        return TRAP_TYPE.pit_trap


class SpikeTrap(Trap):
    def init(self, level):
        Trap.init(self, "Spike Trap", level)

    def get_type(self):
        return TRAP_TYPE.spike_trap


class BoulderTrap(Trap):
    def init(self, level):
        Trap.init(self, "Boulder Trap", level)

    def get_type(self):
        return TRAP_TYPE.boulder_trap


class DartTrap(Trap):
    def init(self, level):
        Trap.init(self, "Dart Trap", level)

    def get_type(self):
        return TRAP_TYPE.dart_trap


class NarrowBridge(Trap):
    def init(self, level):
        Trap.init(self, "Narrow Bridge", level)

    def get_type(self):
        return TRAP_TYPE.narrow_bridge


