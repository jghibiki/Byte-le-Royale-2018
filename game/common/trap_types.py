import random

from game.common.trap import Trap

class TRAP_TYPE:
    pit_trap = 1


def get_trap(trap_type):
    if trap_type == TRAP_TYPE.pit_trap:
        return PitTrap()

def get_random_trap():
    trap_type = random.choice([
        TRAP_TYPE.pit_trap
    ])

    return get_trap(trap_type)



class PitTrap(Trap):
    def init(self, level):
        Trap.init(self, "Pit Trap", level)

    def get_type(self):
        return TRAP_TYPE.pit_trap
