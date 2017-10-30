import random

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

        self.health = 5
        self.damage = 5

    def get_type(self):
        return MON_TYPE.chimera


class Beholder(Monster):
    def init(self, level):
        Monster.init(self, "Beholder", level)


    def get_type(self):
        return MON_TYPE.beholder

class Goblin(Monster):
    def init(self, level):
        Monster.init(self, "Goblin", level)

        self.health = 1
        self.damage = 1

    def get_type(self):
        return MON_TYPE.goblin

