import math

from game.common.enums import *
from game.common.unit import *

special_abilities = {}

def get_special_ability(unit_class):
    global special_abilities

    # melee units

    if unit_class == UnitClass.knight:
        if UnitClass.knight not in special_abilities:
            special_abilities[UnitClass.knight] = Taunt()
        return special_abilities[UnitClass.knight]

    elif unit_class == UnitClass.brawler:
        if UnitClass.brawler not in special_abilities:
            special_abilities[UnitClass.brawler] = FitOfRage()
        return special_abilities[UnitClass.brawler]

    elif unit_class == UnitClass.pikeman:
        if UnitClass.pikeman not in special_abilities:
            special_abilities[UnitClass.pikeman] = TargetWeakness()
        return special_abilities[UnitClass.pikeman]

    # magic units

    elif unit_class == UnitClass.magus:
        if UnitClass.magus not in special_abilities:
            special_abilities[UnitClass.magus] = ElementalBurst()
        return special_abilities[UnitClass.magus]

    elif unit_class == UnitClass.wizard:
        if UnitClass.wizard not in special_abilities:
            special_abilities[UnitClass.wizard] = Invigorate()
        return special_abilities[UnitClass.wizard]

    elif unit_class == UnitClass.sorcerer:
        if UnitClass.sorcerer not in special_abilities:
            special_abilities[UnitClass.sorcerer] = Illusion()
        return special_abilities[UnitClass.sorcerer]

    elif unit_class == UnitClass.alchemist:
        if UnitClass.alchemist not in special_abilities:
            special_abilities[UnitClass.alchemist] = Resupply()
        return special_abilities[UnitClass.alchemist]

def reset_special_abilities():
    global special_abilities
    for _, sa in special_abilities.items():
        sa.reset()



class SpecialAbility:

    def __init__(self):
        self.charged = False

        self.cooldown_timer = 0
        self.charge_timer = 0

        self.target = None


    def cooldown(self):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

    def charge(self):
        if self.charge_timer > 0:
            self.charge -= 1

    def set_target(self, target):
        self.target = target

    def reset(self):
        pass

class Taunt(SpecialAbility):

    def use(self, damage, targets, unit, monster):
        blocked_damage = 0

        if type(targets) is list or type(targets) is tuple:
            # Deal Damage to other units
            original = damage
            damage = math.floor(damage * 0.5)
            for target in targets:
                blocked_damage += origin - damage
                if target is not self:
                    target.current_health -= damage
                    if target.current_health < 0: target.current_health = 0

                    print("{0} deals {1} damage to {2}".format(
                        monster.name,
                        damage,
                        unit.name))
        else:
            # Calculate Damage
            original = damage
            damage = math.floor(damage * 0.85)

        blocked_damage += original - damage

        # Apply Damage to self
        unit.current_health -= damage
        if unit.current_health < 0: unit.current_health = 0

        print("{0} deals {1} damage to {2}".format(
            monster.name,
            damage,
            unit.name))
        print("{0} blocked {1} damage due to taunt.".format(unit.name, blocked_damage))


class FitOfRage(SpecialAbility):

    def __init__(self):
        SpecialAbility.__init__(self)

        self.damage_taken = 0

    def use(self, unit, monster):

        if not self.charged:
            self.damage_taken += damage

        else:
            n = 1.0
            if math.floor(self.health * 0.25) < self.damage_taken < math.floor(self.health * 0.5):
                n = 2.0
            elif math.floor(self.health * 0.5) < self.damage_taken < math.floor(self.health * 75):
                n = 3.0
            elif damage > math.floor(self.health * 0.75):
                n = 3.5

            monster.current_health = math.floor( unit.primary_weapon.damage * ( 2.5 + ( n * 0.5) ) )
            if monster.current_health < 0: monster.current_health= 0

            self.reset()

    def reset(self):
        self.ability_charged = False
        self.special_ability_timer = 0
        self.damage_taken = 0


class TargetWeakness(SpecialAbility):

    def use(self, unit, monster):
        if not self.ability_charged:
            self.charged = True

        else:
            self.charged = False

            monster.current_health = math.floor( unit.primary_weapon.damage * 2.5 )
            if monster.current_health < 0: monster.current_health = 0

    def reset(self):
        self.charged = False


class ElementalBurst(SpecialAbility):

    def charge(self):
        self.charge_timer -= 1
        if self.charge_timer <= 0:
            self.charged = True

    def use(self, unit, monster):

        if not self.ability_charged:
            self.charge_timer = 2

        else:
            dmg_multiplier = 1.0
            for damage_type in [ DamageType.cold, DamageType.fire, DamageType.electricity ]:
                if damage_type in monster.weaknesses:
                    dmg_multiplier += 0.25

            monster.current_health = math.floor( self.primary_weapon.damage * dmg_multiplier )
            if monster.current_health < 0: monster.current_health = 0

            self.reset()

    def reset(self):
        self.charged = False
        self.charge_timer = 0

class Invigorate(SpecialAbility):

    def use(self, target):
        if self.cooldown_timer <= 0:
            target.invigorated = True
            self.cooldown_timer = 3

class Illusion(SpecialAbility):

    def __init__(self):
        SpecialAbility.__init__(self)
        self.target_1 = None
        self.target_2 = None

    def use(self, target_1, target_2):
        if self.cooldown_timer <= 0:
            self.cooldown_timer = 5
            self.target_1 = target_1
            self.target_2 = target_2

    def reset(self):
        self.target_1 = None
        self.target_2 = None

class Resupply(SpecialAbility):

    def use(self, unit, bomb_type):
        pass


class CombatManager:

    def __init__(self, monster, units):
        self.round = 1

        self.monster = monster
        self.units = units

        self.done = False
        self.done_reason = ""
        self.success = None

        # reset special abilities
        reset_special_abilities()


    def serialize_combat_state(self, first=False, last=False):
        data = {}

        if first:
            data["message_type"] = MessageType.combat_begin
        elif last:
            data["message_type"] = MessageType.combat_end
        else:
            data["message_type"] = MessageType.combat_round

        data["monster"] = self.monster.to_dict()

        data["units"] = []
        for u in self.units:
            d = u.to_dict()
            data["units"].append(d)

        return data



    def play_round(self):
        living_units = [ u for u in self.units if u.is_alive() ]

        # pick targets / moves
        monster_target = self.monster.attack(living_units)
        monster_damage = self.monster.damage

        taunt_unit = None

        # handle special abilities early
        for unit in self.units:
            if unit.combat_action == CombatAction.special_ability:
                sa = get_special_ability(unit.unit_class)
                if unit.unit_class is UnitClass.knight:
                    taunt_unit = [ unit, sa ]

        # Apply monster damage
        if taunt_unit is not None:
            taunt_unit[1].use(monster_damage, monster_target, taunt_unit[0], self.monster)
        else:
            if len(monster_target) == 1:
                monster_target = [ monster_target ]

            for mt in monster_target:
                mt.current_health -= monster_damage

                if mt.current_health < 0:
                    mt.current_health = 0

                print("{0} deals {1} damage to {2}".format(
                    self.monster.name,
                    monster_damage,
                    mt.name))


        # apply unit damage to monster
        for unit in self.units:
            dmg = 0
            weapon = None


            # get appropriate weapon
            if unit.combat_action == CombatAction.primary_weapon:
                print("{} uses primary weapon".format(unit.name))
                weapon = unit.primary_weapon
            elif unit.combat_action == CombatAction.secondary_1 and unit.item_slots > 0 and unit.items[0] is not None:

                if unit.class_type in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer]:
                    print("{} uses {}".format(unit.name, unit.spell_1.name))
                    weapon = unit.spell_1

                elif unit.class_type in [ UnitClass.rogue, UnitClass.alchemist]:
                    print("{} uses {}".format(unit.name, unit.bomb_1.name))
                    weapon = unit.bomb_1

            elif unit.combat_action == CombatAction.secondary_2 and unit.item_slots > 1 and unit.items[1] is not None:

                if unit.class_type in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer]:
                    print("{} uses {}".format(unit.name, unit.spell_2.name))
                    weapon = unit.spell_2

                elif unit.class_type in [ UnitClass.rogue, UnitClass.alchemist]:
                    print("{} uses {}".format(unit.name, unit.bomb_2.name))
                    weapon = unit.bomb_2

            elif unit.combat_action == CombatAction.secondary_3 and unit.item_slots > 2 and unit.items[2] is not None:

                if unit.class_type in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer]:
                    print("{} uses {}".format(unit.name, unit.spell_3.name))
                    weapon = unit.spell_3

                elif unit.class_type == UnitClass.rogue:
                    print("{} uses {}".format(unit.name, unit.bomb_3.name))
                    weapon = unit.bomb_3

            elif unit.combat_action == CombatAction.secondary_4 and unit.item_slots > 3 and unit.items[3] is not None:

                if unit.class_type in [ UnitClass.magus, UnitClass.wizard, UnitClass.sorcerer ]:
                    print("{} uses {}".format(unit.name, unit.spell_3.name))
                    weapon = unit.spell_4


            # calculate normal combat damage
            if weapon is not None:
                dmg_multiplier = 1.0
                for damage_type in weapon.damage_types:
                    if damage_type in self.monster.weaknesses:
                        dmg_multiplier += 0.25

                # apply damage * damage multiplier
                dmg += math.floor(weapon.damage * dmg_multiplier)

                print("{0} deals {1} damage to {2}".format(
                    unit.name,
                    dmg,
                    self.monster.name))

                self.monster.current_health -= dmg

                if self.monster.current_health < 0:
                    self.monster.current_health = 0
                    break



        self.round += 1

        if self.monster.current_health <= 0:
            self.done = True
            self.done_reason = "Monster Defeated!"
            self.success = True

        if sum( int(u.is_alive()) for u in self.units ) == 0:
            self.done = True
            self.done_reason = "Party Defeated!\n Game Over!"
            self.success = False


    def print_summary(self):

        print()
        print("Combat Round {}".format(self.round-1))
        print(self.monster.summary())

        print()
        for u in units:
            print(u.summary())


