import random
import math

from game.common.enums import *
from game.common.monster import Monster



def get_monster(monster_type):
    if monster_type == MonsterType.wisp:
        return Wisp()
    elif monster_type == MonsterType.beholder:
        return Beholder()
    elif monster_type == MonsterType.dragon:
        return Dragon()
    elif monster_type == MonsterType.minotaur:
        return Minotaur()
    elif monster_type == MonsterType.slime:
        return Slime()
    elif monster_type == MonsterType.wraith:
        return Wraith()
    elif monster_type == MonsterType.vampire:
        return Vampire()

def get_random_monster(level):
    mon =  random.choice([
        MonsterType.wisp,
        MonsterType.beholder,
        MonsterType.dragon,
        MonsterType.minotaur,
        MonsterType.slime,
        MonsterType.wraith,
        MonsterType.vampire
    ])

    return get_monster(mon)


class Wisp(Monster):
    def init(self, level):
        Monster.init(self, "Wisp", MonsterType.wisp, level)

        self.health = math.floor( ((117500*level)/9) + (94000/9) )
        self.current_health = self.health
        self.damage = math.floor( ((320 * level)/9) + (1120/9) )
        self.gold = math.floor( ((6568 * level)/9) - (4768/9) )

        self.weaknesses = [
            DamageType.cold,
            DamageType.force,
            DamageType.sonic
        ]

        self.attack_state["group_1"] = [
            UnitClass.rogue,
            UnitClass.sorcerer,
            UnitClass.magus,
            UnitClass.wizard,
            UnitClass.alchemist
        ]
        random.shuffle(self.attack_state["group_1"])

        self.attack_state["group_2"] = [
            UnitClass.knight,
            UnitClass.brawler,
            UnitClass.pikeman
        ]
        random.shuffle(self.attack_state["group_2"])

        self.attack_state["index"] = 0

    def attack(self, targets):

        for group in [self.attack_state["group_1"], self.attack_state["group_2"]]:
            while True:
                unit_class_to_target = group[self.attack_state["index"]]

                for unit in targets:
                    if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                        return unit

                self.attack_state["index"] += 1

                if self.attack_state["index"] >= len(group):
                    self.attack_state["index"] = 0
                    break

        raise Exception("No valid targets: ", targets)


class Beholder(Monster):
    def init(self, level):
        Monster.init(self, "Beholder", MonsterType.beholder, level)


        self.health = math.floor( ((125000*level)/9)+(100000/9) )
        self.current_health = self.health
        self.damage = math.floor( (39 * level) +150 )
        self.gold = math.floor( (850 * level) - (500) )

        self.weaknesses = [
            DamageType.acid,
            DamageType.cold,
            DamageType.fire,
            DamageType.piercing,
            DamageType.slashing
        ]

        self.attack_state["index"] = 0

    def attack(self, targets):

        for _ in range(8):

            idx = self.attack_state["index"]
            unit = list(sorted(targets, key=lambda t: t.name))[idx]


            if self.attack_state["index"] >= len(targets):
                self.attack_state["index"] = 0

            if unit.current_health > 0:
                return unit
            else:
                self.attack_state["index"] += 1


class Dragon(Monster):
    def init(self, level):
        Monster.init(self, "Dragon", MonsterType.dragon, level)


        self.health = math.floor( ((50000 * level)/3) + (40000/3) )
        self.current_health = self.health
        self.damage = math.floor( ((370 * level)/9) + (1295/9) )
        self.gold = math.floor( ((9535*level)/9) - (5440/9) )

        self.weaknesses = [
            DamageType.acid,
            DamageType.electricity,
            DamageType.piercing,
            DamageType.precision,
            DamageType.sonic
        ]

        self.attack_state["group"] = [
            UnitClass.knight,
            UnitClass.pikeman,
            UnitClass.alchemist,
            UnitClass.brawler,
            UnitClass.magus,
            UnitClass.rogue,
            UnitClass.wizard,
            UnitClass.sorcerer
        ]

        self.attack_state["index"] = 0

    def attack(self, targets):

        while True:
            unit_class_to_target = self.attack_state["group"][self.attack_state["index"]]

            for unit in targets:
                if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                    return unit

            self.attack_state["index"] += 1

            if self.attack_state["index"] >= len(self.attack_state["group"]):
                self.attack_state["index"] = 0
                break

        raise Exception("No valid targets: ", targets)


class Minotaur(Monster):
    def init(self, level):
        Monster.init(self, "Minotaur", MonsterType.minotaur, level)

        self.health = math.floor( ((140000*level)/9) + (112000/9) )
        self.current_health = self.health
        self.damage = math.floor( ((400 * level)/9) + (1400/9) )
        self.gold = math.floor( ((8500*level)/9) - (4900/9) )

        self.weaknesses = [
            DamageType.cold,
            DamageType.electricity,
            DamageType.precision
        ]

        self.attack_state["group_1"] = [
            UnitClass.knight,
            UnitClass.brawler,
            UnitClass.pikeman,
            UnitClass.rogue
        ]
        random.shuffle(self.attack_state["group_1"])

        self.attack_state["group_2"] = [
            UnitClass.magus,
            UnitClass.sorcerer,
            UnitClass.wizard,
            UnitClass.alchemist
        ]
        random.shuffle(self.attack_state["group_2"])

        self.attack_state["index"] = 0

    def attack(self, targets):

        for group in [self.attack_state["group_1"], self.attack_state["group_2"]]:
            while True:
                unit_class_to_target = group[self.attack_state["index"]]

                for unit in targets:
                    if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                        return unit

                self.attack_state["index"] += 1

                if self.attack_state["index"] >= len(group):
                    self.attack_state["index"] = 0
                    break

        raise Exception("No valid targets: ", targets)


class Slime(Monster):
    def init(self, level):
        Monster.init(self, "Slime", MonsterType.slime, level)

        self.health = math.floor( ((110000*level)/9) + (88000/9) )
        self.current_health = self.health
        self.damage = math.floor( ((100 * level)/3) + (350/3) )
        self.gold = math.floor( ((5740*level)/3) - (3940/9) )

        self.weaknesses = [
            DamageType.electricity,
            DamageType.precision,
            DamageType.sonic
        ]

        self.attack_state["group"] = [
            UnitClass.knight,
            UnitClass.pikeman,
            UnitClass.alchemist,
            UnitClass.brawler,
            UnitClass.magus,
            UnitClass.rogue,
            UnitClass.wizard,
            UnitClass.sorcerer
        ]
        random.shuffle(self.attack_state["group"])

        self.attack_state["index"] = 0

    def attack(self, targets):

        while True:

            if self.attack_state["index"] >= len(self.attack_state["group"]):
                self.attack_state["index"] = 0

            unit_class_to_target = self.attack_state["group"][self.attack_state["index"]]

            for unit in targets:
                if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                    self.attack_state["index"] += 1
                    return unit

            self.attack_state["index"] += 1


        raise Exception("No valid targets: ", targets)


class Wraith(Monster):
    def init(self, level):
        Monster.init(self, "Wraith", MonsterType.wraith, level)

        self.damage = math.floor( ((110 * level)/3) + (385/3) )
        self.health = math.floor( ((130000*level)/9) + (104000/9) )
        self.current_health = self.health
        self.gold = math.floor( ((7048*level)/9) - (4798/9) )

        self.weaknesses = [
            DamageType.acid,
            DamageType.bludgeoning,
            DamageType.fire,
            DamageType.slashing
        ]

        self.attack_state["group_1"] = [
            UnitClass.magus,
            UnitClass.sorcerer,
            UnitClass.wizard,
            UnitClass.alchemist
        ]
        random.shuffle(self.attack_state["group_1"])

        self.attack_state["group_2"] = [
            UnitClass.knight,
            UnitClass.brawler,
            UnitClass.pikeman,
            UnitClass.rogue
        ]
        random.shuffle(self.attack_state["group_2"])

        self.attack_state["index"] = 0

    def attack(self, targets):

        for group in [self.attack_state["group_1"], self.attack_state["group_2"]]:
            while True:
                unit_class_to_target = group[self.attack_state["index"]]

                for unit in targets:
                    if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                        return unit

                self.attack_state["index"] += 1

                if self.attack_state["index"] >= len(group):
                    self.attack_state["index"] = 0
                    break

        raise Exception("No valid targets: ", targets)


class Vampire(Monster):
    def init(self, level):
        Monster.init(self, "Vampire", MonsterType.vampire, level)

        self.health = math.floor( ((125000*level)/9)+(100000/9) )
        self.current_health = self.health
        self.damage = math.floor( ((350 * level)/9) + (1225/9) )
        self.gold = math.floor( ((2474*level)/3) - (1574/3) )

        self.weaknesses = [
            DamageType.fire,
            DamageType.piercing,
            DamageType.precision,
            DamageType.slashing
        ]

        self.attack_state["group_1"] = [
            UnitClass.knight,
            UnitClass.brawler,
            UnitClass.pikeman
        ]
        random.shuffle(self.attack_state["group_1"])

        self.attack_state["group_2"] = [
            UnitClass.rogue,
            UnitClass.sorcerer,
            UnitClass.magus,
            UnitClass.wizard,
            UnitClass.alchemist
        ]
        random.shuffle(self.attack_state["group_2"])

        self.attack_state["index"] = 0

    def attack(self, targets):

        for group in [self.attack_state["group_1"], self.attack_state["group_2"]]:
            self.attack_state["index"] = 0
            while True:
                unit_class_to_target = group[self.attack_state["index"]]

                for unit in targets:
                    if unit.unit_class == unit_class_to_target and unit.current_health > 0:
                        return unit

                self.attack_state["index"] += 1

                if self.attack_state["index"] >= len(group):
                    self.attack_state["index"] = 0
                    break

        raise Exception("No valid targets: ", targets)

