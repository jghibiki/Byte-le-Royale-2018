import random

from game.common.trap import Trap

class TRAP_TYPE:
    pit_trap = 1


def get_random_trap(self):
    return random.choice([
        TRAP_TYPE.pit_trap
    ])


class PitTrap(Trap):
    def init(self, level):
        Trap.init(self, "Pit Trap", level)
