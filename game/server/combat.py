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

def cooldown_abilities(self):
    global special_abilities
    for _, sa in special_abilities.items():
        sa.cooldown()


class SpecialAbility:

    def __init__(self):
        self.charged = False
        self.charging = False

        self.cooldown_timer = 0
        self.charge_timer = 0

        self.target = None


    def cooldown(self):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

    def charge(self):
        if self.charge_timer > 0:
            self.charge_timer -= 1

    def set_target(self, target):
        self.target = target

    def reset(self):
        pass

class Taunt(SpecialAbility):

    def use(self, damage, targets, unit, monster):
        pass


class FitOfRage(SpecialAbility):

    def __init__(self):
        SpecialAbility.__init__(self)

        self.damage_taken = 0

    def use(self, unit, monster, damage):

        if not self.charged:
            print("{0} is becoming enraged".format(unit.name))
            self.damage_taken += damage

            if not self.charging:
                self.charge_timer = 1
                self.charging = True
            else:
                self.charge_timer -= 1
                if self.charge_timer <= 0:
                    self.charging = False
                    self.charged = True
        else:
            n = 1.0
            if math.floor(unit.health * 0.25) < self.damage_taken < math.floor(unit.health * 0.5):
                n = 2.0
            elif math.floor(unit.health * 0.5) < self.damage_taken < math.floor(unit.health * 75):
                n = 3.0
            elif damage > math.floor(unit.health * 0.75):
                n = 3.5

            damage = math.floor( unit.primary_weapon.damage * ( 3.5 + n  ) )
            monster.current_health -= damage
            if monster.current_health < 0: monster.current_health = 0

            print("In a Fit of Rage, {0} deals {1} damage to {2}".format(unit.name, damage, monster.name))

            self.reset()

    def reset(self):
        self.charged = False
        self.charging = False
        self.charge_timer = 0
        self.damage_taken = 0


class TargetWeakness(SpecialAbility):

    def use(self, unit, monster):
        if not self.charged:
            self.charged = True
            print("{} searches {} for weaknesses.".format(unit.name, monster.name))

        else:
            self.charged = False

            damage = math.floor( unit.primary_weapon.damage * 2.5 )
            monster.current_health -= damage
            if monster.current_health < 0: monster.current_health = 0

            print("Seeing a weakness, {} strikes at {} for {} damage.".format(unit.name, monster.name, damage))

    def reset(self):
        self.charged = False


class ElementalBurst(SpecialAbility):

    def use(self, unit, monster):

        if not self.charged:
            print("{0} charges up magical energy.".format(unit.name))
            if not self.charging:
                self.charge_timer = 2
                self.charging = True
            else:
                self.charge_timer -= 1
                if self.charge_timer <= 0:
                    self.charged = True
                    self.charging = False

        else:
            dmg_multiplier = 2.0
            for damage_type in [ DamageType.cold, DamageType.fire, DamageType.electricity ]:
                if damage_type in monster.weaknesses:
                    dmg_multiplier += 0.25

            damage = math.floor( unit.primary_weapon.damage * dmg_multiplier )
            monster.current_health -= damage
            if monster.current_health < 0: monster.current_health = 0

            print("With a burst of elemental energy, {0} deals {1} damage to {2}".format(unit.name, damage, monster.name))

            self.reset()

    def reset(self):
        self.charged = False
        self.charging = False
        self.charge_timer = 0

class Invigorate(SpecialAbility):

    def use(self):
        if self.cooldown_timer <= 0:
            self.cooldown_timer = 3
        else:
            self.cooldown_timer -= 1

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
        brawler_damage = 0
        invigorated_unit = None

        # handle early special abilities
        for unit in self.units:
            if unit.combat_action == CombatAction.special_ability:
                sa = get_special_ability(unit.unit_class)

                if unit.unit_class is UnitClass.knight:
                    taunt_unit = unit

                elif unit.unit_class == UnitClass.wizard:
                    print("We have a wizard!")
                    if sa.cooldown_timer <= 0:
                        print("Wizard's ability is good to go")
                        print(unit.combat_action_target_1)
                        for u in self.units:
                            print(u.id)
                            if u.id == unit.combat_action_target_1:
                                invigorated_unit = u
                                break
                        if invigorated_unit is not None:
                            print("{0} casts invigorate on {1}".format(unit.name, invigorated_unit.name))

        # verify that invigorated_unit is not taunt_unit
        if invigorated_unit is not None:
            if taunt_unit is not None  and taunt_unit == invigorated_unit:
                # cancel taunt if unit is invigorated
                taunt_unit = None


        # Apply monster damage
        if taunt_unit is not None:
            # Knight Taunt ability implementation
            blocked_damage = 0

            if type(monster_target) is list or type(monster_target) is tuple:
                # Deal Damage to other units
                damage = math.floor(monster_damage * 0.5)
                for target in monster_target:
                    blocked_damage += monster_damage - damage

                    if target.unit_class is UnitClass.brawler:
                        # record brawler damage
                        brawler_damage += damage

                    if target is not self:
                        target.current_health -= damage
                        if target.current_health < 0: target.current_health = 0

                        print("{0} deals {1} damage to {2}".format(
                            self.monster.name,
                            damage,
                            target.name))
            else:
                # Calculate Damage
                damage = math.floor(monster_damage * 0.85)

            blocked_damage += monster_damage - damage

            # Apply Damage to self
            taunt_unit.current_health -= damage
            if taunt_unit.current_health < 0: taunt_unit.current_health = 0

            print("{0} deals {1} damage to {2}".format(
                self.monster.name,
                damage,
                taunt_unit.name))
            print("{0} blocked {1} damage due to taunt.".format(taunt_unit.name, blocked_damage))

        else:
            # Normal Damage ( without taunt) implementation
            if type(monster_target) is not list:
                monster_target = [ monster_target ]

            for u in monster_target:
                u.current_health -= monster_damage

                if u.unit_class is UnitClass.brawler:
                    # record brawler damage
                    brawler_damage += monster_damage

                if u.current_health < 0:
                    u.current_health = 0

                print("{0} deals {1} damage to {2}".format(
                    self.monster.name,
                    monster_damage,
                    u.name))


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

            elif unit.combat_action == CombatAction.special_ability:
                sa = get_special_ability(unit.unit_class)

                if unit.unit_class is UnitClass.brawler:
                    sa.use(unit, self.monster, brawler_damage)

                elif unit.unit_class is UnitClass.pikeman:
                    sa.use(unit, self.monster)

                elif unit.unit_class is UnitClass.magus:
                    sa.use(unit, self.monster)

                elif unit.unit_class is UnitClass.wizard:
                    sa.use()




            # calculate normal combat damage
            if weapon is not None:
                dmg_multiplier = 1.0

                if unit is invigorated_unit: # deal more damage if target was invigorated
                    dmg_multiplier += 1.5

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


