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

def get_random_monster(level):
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

        # config values
        damage = 250
        damage_scale = 0.5
        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.slashing,
            DamageType.electricity,
            DamageType.cold
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

        # config values
        damage = 250
        damage_scale = 0.5
        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.piercing,
            DamageType.slashing,
            DamageType.acid,
            DamageType.cold,
            DamageType.fire
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

        # config values
        damage = 250
        damage_scale = 0.5
        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.piercing,
            DamageType.slashing,
            DamageType.acid,
            DamageType.cold,
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

        # config values
        damage = 250
        damage_scale = 0.5
        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.slashing,
            DamageType.bludgeoning,
            DamageType.acid,
            DamageType.electricity,
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

        # config values
        damage = 175
        damage_scale = 0.55
        health = 100000
        health_scale = 0.35
        gold = 235
        gold_scale = 0.45

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.piercing,
            DamageType.bludgeoning,
            DamageType.cold,
            DamageType.fire,
            DamageType.electricity
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


class Goblin(Monster):
    def init(self, level):
        Monster.init(self, "Goblin", MonsterType.goblin, level)

        # config values
        damage = 250
        damage_scale = 0.5

        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

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

        # config values
        damage = 150
        damage_scale = 0.5
        health = 100000
        health_scale = 0.25
        gold = 200
        gold_scale = 0.75

        self.health = math.floor(health * ((health_scale * (level-1)) + 1))
        self.current_health = self.health
        self.damage = math.floor(damage * ((damage_scale * (level-1)) + 1))
        self.gold = math.floor(gold * ((gold_scale * (level-1)) + 1))

        self.weaknesses = [
            DamageType.piercing,
            DamageType.fire,
            DamageType.electricity,
            DamageType.sonic
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

