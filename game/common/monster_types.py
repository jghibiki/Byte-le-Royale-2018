from game.common.monster import Monster

class MON_TYPE:
    chimera = 1
    beholder = 2
    goblin = 3


def get_random_monster(self):
    return random.choice([
        MON_TYPE.chimera,
        MON_TYPE.beholder,
        MON_TYPE.goblin
    ])


class Chimera(Monster):
    def init(self, level):
        Monster.init(self, "Chimera", level)


class Beholder(Monster):
    def init(self, level):
        Monster.init(self, "Beholder", level)

class Goblin(Monster):
    def init(self, level):
        Monster.init(self, "Goblin", level)

