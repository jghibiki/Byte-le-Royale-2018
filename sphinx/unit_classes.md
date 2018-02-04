# Unit Classes

## Knight

![](_static/knight.png)

```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 17000  | Sword          | 10    | 14        |
+--------+----------------+-------+-----------+
```

**Unique Ability:** Taunt: If a monster attacks one unit, this unit absorbs 85% damage from the attack and the original target takes none. If a monster attacks multiple units, this unit absorbs 50% of the total damage that would be dealt to each unit. Each unit that was originally targeted receives 50% of the damage originally intended for them.

### Unit Properties
- ```Knight.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Knight.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Knight.attack()``` Attack monster with Sword.
- ```Knight.taunt()``` Use Taunt ability.
- ```Knight.wait()``` Do nothing for this turn.

## Brawler

![](_static/brawler.png)

```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 15000  | Mace           | 10    | 14        |
+--------+----------------+-------+-----------+
```

**Unique Ability:** Fit of Rage: This unit deals takes two turns to become enraged. Damage dealt to this unit while becoming enraged increases the effectiveness of Fit of Rage. Once enraged, this unit will deal ```(normal damage) * (2.5 + (N * 0.5))``` damage. Where N is determined by the table below.


```eval_rst
+------------------+--------------------------------------------------------------+
| N                | Damage Taken                                                 |
+==================+==============================================================+
| 0                | damage < (unit max health) * 0.25                            |
+------------------+--------------------------------------------------------------+
| 1                | (unit max health) * 0.25 <= damage < (unit max health) * 0.5 |
+------------------+--------------------------------------------------------------+
| 2                | damage >= (unit max health) * 0.75                           |
+------------------+--------------------------------------------------------------+
```

### Unit Properties
- ```Brawler.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Brawler.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Brawler.attack()``` Attack monster with Mace.
- ```Brawler.fit_of_rage()``` Use Fit of Rage ability.
- ```Brawler.wait()``` Do nothing for this turn.

## Pikeman

![](_static/pikeman.png)

```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 16000  | Spear          | 10    | 14        |
+--------+----------------+-------+-----------+
```

**Unique Ability:** Target Weakness: take a turn to find critical points, then next turn deal 2.5 * damage.

### Unit Properties
- ```Pikeman.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Pikeman.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Pikeman.attack()``` Attack monster with Spear.
- ```Pikeman.target_weakness()``` Use Target Weakness ability.
- ```Pikeman.wait()``` Do nothing for this turn.

## Rogue

![](_static/rogue.png)

```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Bomb Slots  |
+========+================+=======+===========+=============+
| 14000  | Dagger         | 30    | 30        | 3           |
+--------+----------------+-------+-----------+-------------+
```

**Unique Ability:** Trap expert: rogues have increased focus and willpower during trap evasion.

### Unit Properties
- ```Rogue.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Rogue.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.
- ```Rogue.bomb_1``` The type of bomb stored in bomb slot 1.
- ```Rogue.bomb_1_quantity``` The quantity of bombs stored in bomb slot 1. When a bomb is used this number wil decrease, if it is zero, the unit will not be able to use this bomb type.
- ```Rogue.bomb_2``` The type of bomb stored in bomb slot 2.
- ```Rogue.bomb_2_quantity``` The quantity of bombs stored in bomb slot 2. When a bomb is used this number wil decrease, if it is zero, the unit will not be able to use this bomb type.
- ```Rogue.bomb_3``` The type of bomb stored in bomb slot 3.
- ```Rogue.bomb_3_quantity``` The quantity of bombs stored in bomb slot 3. When a bomb is used this number wil decrease, if it is zero, the unit will not be able to use this bomb type.

### Combat Methods
- ```Rogue.attack()``` Attack monster with Dagger.
- ```Rogue.use_bomb_1()``` Attack monster with Bomb in Bomb Slot 1.
- ```Rogue.use_bomb_2()``` Attack monster with Bomb in Bomb Slot 2.
- ```Rogue.use_bomb_3()``` Attack monster with Bomb in Bomb Slot 3.
- ```Rogue.wait()``` Do nothing for this turn.


## Magus

![](_static/magus.png)


```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
| 10000  | Staff          | 14    | 10        | 4           |
+--------+----------------+-------+-----------+-------------+
```

**Unique Ability:** Elemental Burst: Spend two turns concentrating to cast a spell that deals fire, cold, and electric damage at 2 times damage.

### Unit Properties
- ```Magus.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Magus.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Magus.attack()``` Attack monster with Staff.
- ```Magus.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Magus.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Magus.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Magus.use_spell_4()``` Attack monster with Spell in Spell Slot 4.
- ```Magus.elemental_burst()``` Use Elemental Burst ability.
- ```Magus.wait()``` Do nothing for this turn.

## Wizard

![](_static/wizard.png)

```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
| 11000  | Wand           | 14    | 10        | 4           |
+--------+----------------+-------+-----------+-------------+

```

**Unique Ability:** Invigorate: Charm one ally to deal 1.5 times damage for a turn. Cancels any other damage modifiers that would be in effect for that unit including the effects of Elemental Burst, and Fit of Rage. Can be cast once every 3 turns.

### Unit Properties
- ```Wizard.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Wizard.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Wizard.attack()``` Attack monster with Wand.
- ```Wizard.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Wizard.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Wizard.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Wizard.use_spell_4()``` Attack monster with Spell in Spell Slot 4.
- ```Wizard.invigorate(target)``` Use Invigorate ability.
- ```Wizard.wait()``` Do nothing for this turn.

## Sorcerer

![](_static/sorcerer.png)

```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
| 12000  | Spell Book     | 14    | 10        | 4           |
+--------+----------------+-------+-----------+-------------+
```

**Unique Ability:** Illusion: Cast an illusion that disguises one player unit as another on the next turn. Monsters will be unable to tell the difference between the two units for that turn. Can be cast once every 5 turns.

### Unit Properties
- ```Sorcerer.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Sorcerer.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Sorcerer.attack()``` Attack monster with Spell Book.
- ```Sorcerer.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Sorcerer.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Sorcerer.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Sorcerer.use_spell_4()``` Attack monster with Spell in Spell Slot 4.
- ```Sorcerer.illusion(unit_to_disguise, unit_to_be_disguised_as)``` Use Illusion ability. Disguesses the first unit as the second.
- ```Sorcerer.wait()``` Do nothing for this turn.

## Alchemist

![](_static/alchemist.png)

```eval_rst
+--------+---------------------+-------+-----------+------------+
| Health | Primary Weapon      | Focus | Willpower | Bomb Slots |
+========+=====================+=======+===========+============+
| 13000  | Alchemical Supplies | 12    | 10        | 2          |
+--------+---------------------+-------+-----------+------------+
```

**Unique Ability:** Resupply: Spend one turn to regenerate one of bomb of the types currently possessed.

### Unit Properties
- ```Alchemist.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.
- ```Alchemist.bomb_1``` The type of bomb stored in bomb slot 1.
- ```Alchemist.bomb_1_quantity``` The quantity of bombs stored in bomb slot 1. When a bomb is used this number wil decrease, if it is zero, the unit will not be able to use this bomb type.
- ```Alchemist.bomb_2``` The type of bomb stored in bomb slot 2.
- ```Alchemist.bomb_2_quantity``` The quantity of bombs stored in bomb slot 2. When a bomb is used this number wil decrease, if it is zero, the unit will not be able to use this bomb type.

### Combat Methods
- ```Alchemist.use_bomb_1()``` Attack monster with Bomb in Bomb Slot 1.
- ```Alchemist.use_bomb_2()``` Attack monster with Bomb in Bomb Slot 2.
- ```Alchemist.resupply(bomb_type_to_resupply)``` Use Resupply ability.
- ```Alchemist.wait()``` Do nothing for this turn.

*Note: The Alchemist does not have a basic attack.*




