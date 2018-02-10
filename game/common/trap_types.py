import random

from game.common.trap import Trap
from game.common.enums import *



def get_trap(trap_type):
    if trap_type == TrapType.spike_trap:
        return SpikeTrap()
    elif trap_type == TrapType.pendulum_bridge:
        return PendulumBridge()
    elif trap_type == TrapType.falling_ceiling:
        return FallingCeiling()
    elif trap_type == TrapType.puzzle_box:
        return PuzzleBox()
    elif trap_type == TrapType.riddles_of_the_sphinx:
        return RiddlesOfTheSphinx()
    elif trap_type == TrapType.eldritch_barrier:
        return EldritchBarrier()

def get_random_trap():
    trap_type = random.choice([
        TrapType.spike_trap,
        TrapType.falling_ceiling,
        TrapType.puzzle_box ,
        TrapType.pendulum_bridge,
        TrapType.riddles_of_the_sphinx,
        TrapType.eldritch_barrier
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
                  3, # damage interval
                  200, # damage
                  50) # required effort

class FallingCeiling(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.falling_ceiling,
                  "Falling Ceilling",
                  level,
                  TrapStat.will,
                  TrapPassType.group_pass,
                  TrapDamageType.all,
                  3, # damage interval
                  999999, # damage
                  100) # required effort


class PuzzleBox(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.puzzle_box,
                  "Puzzle Box",
                  level,
                  TrapStat.focus,
                  TrapPassType.group_pass,
                  TrapDamageType.lowest_health,
                  1, # damage interval
                  100, # damage
                  150) # required effort


class PendulumBridge(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.pendulum_bridge,
                  "Pendulum Bridge",
                  level,
                  TrapStat.willpower,
                  TrapPassType.group_pass_on_first_success,
                  TrapDamageType.random_one,
                  4, # damage interval
                  200, # damage
                  50) # required effort



class RiddlesOfTheSphinx(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.riddles_of_the_sphinx,
                  "Riddles of the Sphinx",
                  level,
                  TrapStat.focus,
                  TrapPassType.group_pass_on_first_success,
                  TrapDamageType.random_one,
                  2, # damage interval
                  100, # damage
                  100) # required effort


class EldritchBarrier(Trap):
    def init(self, level):
        Trap.init(self,
                  TrapType.eldritch_barrier,
                  "Eldritch Barrier",
                  level,
                  TrapStat.focus,
                  TrapPassType.individual_pass,
                  TrapDamageType.random_one,
                  2, # damage interval
                  150, # damage
                  50) # required effort
