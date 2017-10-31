import random
import math

from game.common.damage import *
from game.common.monster import Monster

class MON_TYPE:
    chimera = 1
    beholder = 2
    goblin = 3


def get_monster(monster_type):
    if monster_type == MON_TYPE.chimera:
        return Chimera()
    elif monster_type == MON_TYPE.beholder:
        return Beholder()
    elif monster_type == MON_TYPE.goblin:
        return Goblin()

def get_random_monster():
    mon =  random.choice([
        MON_TYPE.chimera,
        MON_TYPE.beholder,
        MON_TYPE.goblin
    ])

    return get_monster(mon)


class Chimera(Monster):
    def init(self, level):
        Monster.init(self, "Chimera", level)

        self.health = 9000
        self.current_health = self.health
        self.defense = 750 * math.floor(0.5 * level)
        self.damage = 500 * math.floor(0.5 * level)

        self.weaknesses = [
            DAMAGE_TYPE.slashing,
            DAMAGE_TYPE.cold
        ]

    def get_type(self):
        return MON_TYPE.chimera


class Beholder(Monster):
    def init(self, level):
        Monster.init(self, "Beholder", level)

        self.health = 6000
        self.current_health = self.health
        self.defense = 1500 * math.floor(0.5 * level)
        self.damage = 250 * math.floor(0.5 * level)

        self.weaknesses = [
            DAMAGE_TYPE.piercing,
            DAMAGE_TYPE.slashing,
            DAMAGE_TYPE.acid,
            DAMAGE_TYPE.cold
        ]


    def get_type(self):
        return MON_TYPE.beholder

class Goblin(Monster):
    def init(self, level):
        Monster.init(self, "Goblin", level)

        self.health = 6000
        self.current_health = self.health
        self.defense = 500 * level
        self.damage = 1000 * level

        self.weaknesses = [
            DAMAGE_TYPE.piercing,
            DAMAGE_TYPE.slashing,
            DAMAGE_TYPE.acid,
            DAMAGE_TYPE.cold,
            DAMAGE_TYPE.fire,
            DAMAGE_TYPE.electricity
        ]

    def get_type(self):
        return MON_TYPE.goblin

