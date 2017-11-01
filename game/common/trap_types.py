import random

from game.common.trap import Trap

class TRAP_TYPE:
    pit_trap = 1
    spike_trap = 2
    boulder_trap = 3
    dart_trap = 4
    narrow_bridge = 5



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
    def init(self):
        Trap.init(self, "Pit Trap")

        self.counters = [

        ]

    def get_type(self):
        return TRAP_TYPE.pit_trap


class SpikeTrap(Trap):
    def init(self):
        Trap.init(self, "Spike Trap")

    def get_type(self):
        return TRAP_TYPE.spike_trap


class BoulderTrap(Trap):
    def init(self):
        Trap.init(self, "Boulder Trap")

    def get_type(self):
        return TRAP_TYPE.boulder_trap


class DartTrap(Trap):
    def init(self):
        Trap.init(self, "Dart Trap")

    def get_type(self):
        return TRAP_TYPE.dart_trap


class NarrowBridge(Trap):
    def init(self):
        Trap.init(self, "Narrow Bridge")

    def get_type(self):
        return TRAP_TYPE.narrow_bridge


