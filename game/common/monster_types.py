import random
import math

from game.common.enums import *
from game.common.monster import Monster



def get_monster(monster_type):
    if monster_type == MonsterType.wisp:
        return Wisp()
    elif monster_type == MonsterType.beholder:
        return Beholder()
    #elif monster_type == MonsterType.goblin:
    #    return Goblin()
    elif monster_type == MonsterType.dragon:
        return Dragon()
    elif monster_type == MonsterType.minotaur:
        return Minotaur()
    elif monster_type == MonsterType.slime:
        return Slime()
    elif monster_type == MonsterType.wraith:
        return Wraith()

def get_random_monster():
    mon =  random.choice([
        MonsterType.wisp,
        MonsterType.beholder,
    #    MonsterType.goblin,
        MonsterType.dragon,
        MonsterType.minotaur,
        MonsterType.slime,
        MonsterType.wraith
    ])

    return get_monster(mon)


class Wisp(Monster):
    def init(self, level):
        Monster.init(self, "Wisp", MonsterType.wisp, level)

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

class Dragon(Monster):
    def init(self, level):
        Monster.init(self, "Dragon", MonsterType.dragon, level)

        self.health = 6000
        self.current_health = self.health
        self.damage = 250 * math.floor(0.5 * level)

        self.weaknesses = [
        ]

class Minotaur(Monster):
    def init(self, level):
        Monster.init(self, "Minotaur", MonsterType.minotaur, level)

        self.health = 6000
        self.current_health = self.health
        self.damage = 250 * math.floor(0.5 * level)

        self.weaknesses = [
        ]

class Slime(Monster):
    def init(self, level):
        Monster.init(self, "Slime", MonsterType.slime, level)

        self.health = 6000
        self.current_health = self.health
        self.damage = 250 * math.floor(0.5 * level)

        self.weaknesses = [
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

class Wraith(Monster):
    def init(self, level):
        Monster.init(self, "Wraith", MonsterType.wraith, level)

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

