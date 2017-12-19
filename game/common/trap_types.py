import random

from game.common.trap import Trap
from game.common.enums import *



def get_trap(trap_type):
    if trap_type == TrapType.spike_trap:
        return SpikeTrap()

def get_random_trap():
    trap_type = random.choice([
        TrapType.spike_trap,
    ])

    return get_trap(trap_type)



class SpikeTrap(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.spike_trap,
                  "Spike Trap",
                  level,
                  TrapStat.will,
                  TrapPassType.individual_pass,
                  TrapDamageType.random_two,
                  1, # damage interval
                  100, # damage
                  300) # required effort




