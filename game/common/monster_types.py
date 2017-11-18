import random
import math

from game.common.enums import *
from game.common.monster import Monster



def get_monster(monster_type):
    if monster_type == MonsterType.chimera:
        return Chimera()
    elif monster_type == MonsterType.beholder:
        return Beholder()
    elif monster_type == MonsterType.goblin:
        return Goblin()

def get_random_monster():
    mon =  random.choice([
        MonsterType.chimera,
        MonsterType.beholder,
        MonsterType.goblin
    ])

    return get_monster(mon)


class Chimera(Monster):
    def init(self, level):
        Monster.init(self, "Chimera", MonsterType.chimera, level)

        self.health = 9000
        self.current_health = self.health
        self.damage = 500 * math.floor(0.5 * level)

        self.weaknesses = [
            DamageType.slashing,
            DamageType.cold
        ]



class Beholder(Monster):
    def init(self, level):
        Monster.init(self, "Beholder", MonsterType.beholder, level)

        self.health = 6000
        self.current_health = self.health
        self.damage = 250 * math.floor(0.5 * level)

        self.weaknesses = [
            DamageType.piercing,
            DamageType.slashing,
            DamageType.acid,
            DamageType.cold
        ]



class Goblin(Monster):
    def init(self, level):
        Monster.init(self, "Goblin", MonsterType.goblin, level)

        self.health = 6000
        self.current_health = self.health
        self.damage = 150 * level

        self.weaknesses = [
            DamageType.piercing,
            DamageType.slashing,
            DamageType.acid,
            DamageType.cold,
            DamageType.fire,
            DamageType.electricity
        ]


