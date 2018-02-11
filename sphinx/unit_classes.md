# Unit Classes

## Knight

![](_static/knight.png)

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 13500  | Sword          | 10    | 14        |
+--------+----------------+-------+-----------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 18750 | 20625 | 22500 | 24375 | 26250 | 28125 | 30000 | 31875 | 33750 | 35625 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Taunt: If a monster attacks one unit, this unit absorbs 85% damage from the attack and the original target takes none. If a monster attacks multiple units, this unit absorbs 50% of the total damage that would be dealt to each unit. Each unit that was originally targeted receives 50% of the damage originally intended for them.

### Unit Properties
- ```Knight.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Knight.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Knight.attack()``` Attack monster with Sword.
- ```Knight.taunt()``` Use Taunt ability.
- ```Knight.wait()``` Do nothing for this turn.

## Brawler

![](_static/brawler.png)

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 12000  | Mace           | 10    | 14        |
+--------+----------------+-------+-----------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 16875 | 18750 | 20625 | 22500 | 24375 | 26250 | 28125 | 30000 | 31875 | 33750 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Fit of Rage: This unit deals takes two turns to become enraged. Damage dealt to this unit while becoming enraged increases the effectiveness of Fit of Rage. Once enraged, this unit will deal ```(normal damage) * (3.5 + N)``` damage. Where N is determined by the table below. NOTE: This must be called, or "charged", for multiple turns. It will execute on the third turn.


```eval_rst
+------------------+--------------------------------------------------------------+
| N                | Damage Taken                                                 |
+==================+==============================================================+
| 2.0              | (unit max health) * 0.25 < damage <= (unit max health) * 0.5 |
+------------------+--------------------------------------------------------------+
| 3.0              | (unit max health) * 0.5 < damage <= (unit max health) * 0.75 |
+------------------+--------------------------------------------------------------+
| 3.5              | damage >= (unit max health) * 0.75                           |
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

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+
| Health | Primary Weapon | Focus | Willpower |
+========+================+=======+===========+
| 12750  | Spear          | 10    | 14        |
+--------+----------------+-------+-----------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 17812 | 19687 | 21562 | 23437 | 25312 | 27187 | 29062 | 30937 | 32812 | 34687 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Target Weakness: takes a turn to find critical points, then next turn deal 2.5 * damage. NOTE: This must be called, or "charged", for multiple turns. It will execute on the second turn.

### Unit Properties
- ```Pikeman.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Pikeman.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Pikeman.attack()``` Attack monster with Spear.
- ```Pikeman.target_weakness()``` Use Target Weakness ability.
- ```Pikeman.wait()``` Do nothing for this turn.

## Rogue

![](_static/rogue.png)

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Bomb Slots  |
+========+================+=======+===========+=============+
| 10000  | Dagger         | 30    | 30        | 3           |
+--------+----------------+-------+-----------+-------------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 14375 | 16250 | 18125 | 20000 | 21875 | 23750 | 25625 | 27500 | 29375 | 31250 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Trap expert: rogues have increased focus and willpower during trap evasion.

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


### Base Stats
```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
|  7000  | Staff          | 14    | 10        | 3           |
+--------+----------------+-------+-----------+-------------+
```

### Armor 
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 10625 | 12500 | 14375 | 16250 | 18125 | 20000 | 21875 | 23750 | 25625 | 27500 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Elemental Burst: Spend two turns concentrating to cast a spell that deals fire, cold, and electric damage at 200% the Magus' primary weapon damage, plus an extra 25% per weakness hit. NOTE: This must be called, or "charged", for multiple turns. It will execute on the second turn.

### Unit Properties
- ```Magus.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Magus.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Magus.attack()``` Attack monster with Staff.
- ```Magus.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Magus.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Magus.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Magus.elemental_burst()``` Use Elemental Burst ability.
- ```Magus.wait()``` Do nothing for this turn.

## Wizard

![](_static/wizard.png)

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
|  8250  | Wand           | 14    | 10        | 3           |
+--------+----------------+-------+-----------+-------------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 12187 | 14062 | 15937 | 17812 | 19687 | 21562 | 23437 | 25312 | 27187 | 29062 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Invigorate: Charm one ally to deal 1.5 times damage for a turn. Cancels any other damage modifiers that would be in effect for that unit including the effects of Elemental Burst, and Fit of Rage. Can be cast once every 3 turns.

### Unit Properties
- ```Wizard.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Wizard.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Wizard.attack()``` Attack monster with Wand.
- ```Wizard.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Wizard.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Wizard.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Wizard.invigorate(target)``` Use Invigorate ability.
- ```Wizard.wait()``` Do nothing for this turn.

## Sorcerer

![](_static/sorcerer.png)

### Base Stats
```eval_rst
+--------+----------------+-------+-----------+-------------+
| Health | Primary Weapon | Focus | Willpower | Spell Slots |
+========+================+=======+===========+=============+
|  7500  | Spell Book     | 14    | 10        | 3           |
+--------+----------------+-------+-----------+-------------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 11250 | 13125 | 15000 | 16875 | 18750 | 20625 | 22500 | 24375 | 26250 | 28125 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Illusion: Cast an illusion that disguises one player unit as another on the next turn. Monsters will be unable to tell the difference between the two units for that turn. Can be cast once every 5 turns.

### Unit Properties
- ```Sorcerer.primary_weapon``` The type of primary weapon the unit is carrying.
- ```Sorcerer.armor``` The type of armor the unit is carrying. Is initially ```None``` until armor is bought for the unit.

### Combat Methods
- ```Sorcerer.attack()``` Attack monster with Spell Book.
- ```Sorcerer.use_spell_1()``` Attack monster with Spell in Spell Slot 1.
- ```Sorcerer.use_spell_2()``` Attack monster with Spell in Spell Slot 2.
- ```Sorcerer.use_spell_3()``` Attack monster with Spell in Spell Slot 3.
- ```Sorcerer.illusion(unit_to_disguise, unit_to_be_disguised_as)``` Use Illusion ability. Disguesses the first unit as the second.
- ```Sorcerer.wait()``` Do nothing for this turn.

## Alchemist

![](_static/alchemist.png)

### Base Stats
```eval_rst
+--------+---------------------+-------+-----------+------------+
| Health | Primary Weapon      | Focus | Willpower | Bomb Slots |
+========+=====================+=======+===========+============+
|  9250  | Alchemical Supplies | 12    | 10        | 2          |
+--------+---------------------+-------+-----------+------------+
```

### Armor
Armor replaces the unit's current maximum health.
```eval_rst
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+
| 13437 | 15312 | 17187 | 19062 | 20937 | 22812 | 24687 | 26562 | 28437 | 30312 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

### Unique Ability
Resupply: Spend one turn to regenerate one of bomb of the types currently possessed.

### Special Ability 
Bomb Expert: The Alchemist can hold three of each bomb type. Additionally, their bomb damage gains bonus damage, which scales with the bomb's level:

```
((level*5)/100) + 1.0
``` 


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




