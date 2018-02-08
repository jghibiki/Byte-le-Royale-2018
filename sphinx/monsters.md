# Monsters & Combat

## Combat

Your party enters a room with a monster, combat will begin. The ```combat_round``` method on the game client will be called, and you will be able to direct your units to take various actions.

### Combat Actions

There are three main types of combat actions, attacking (also sometimes called basic attacking), attacking with a bomb or spells (only allowed by certain unit classes), and using a special ability.

- **Attacking**: The unit attacks using their primary weapon (as listed on the [Unit Classes](/~documentation/unit_classes.html#unit-classes) page).
    - Basic attacking is done using the ```unit.attack()``` method.
- **Bomb or spells**: The unit attacks with an auxiliary item held in bomb or spell slots. Alchemists and rogues can use bombs; the Magus, Wizard, and Sorcerer classes can use spells. These items make use of monster weaknesses which are described below in more detail.
    - To use a bomb or spell, refer to the api for the specific class you are using as listed on the [Unit Classes](/~documentation/unit_classes.html#unit-classes) page.
- **Special Abilities**: Each class - excluding the rogue - has a unique special ability that can be used in combat.
    - To use a special ability, refer to the api for the specific class you are using as listed on the [Unit Classes](/~documentation/unit_classes.html#unit-classes) page.

### Monster Weaknesses & Item Damage Types

Each monsters have a series of weaknesses. These weaknesses are found as a list on the ```monster.weaknesses``` property. Each value in the list is an enum value corresponding to one or more of the following weaknesses:
- ```DamageType.piercing```
- ```DamageType.slashing```
- ```DamageType.bludgeoning```
- ```DamageType.precision```
- ```DamageType.fire```
- ```DamageType.cold```
- ```DamageType.electricity```
- ```DamageType.acid```
- ```DamageType.sonic```
- ```DamageType.force```

Attacking a monster using a weapon, spell, or bomb with a matching weakness will deal double damage to the monster.

## Monster Properties

- ```monster.monster_type```: A MonsterType enum value indicating the type of monster.
- ```monster.level```: The level of the monster.
- ```monster.health```: The monster's max health.
- ```monster.current_health```: The monster's current health.
- ```monster.damage```: The amount of damage the monster deals when it attacks.
- ```monster.gold```: The amount of gold that will rewarded for defeating the monster.

## Monsters

### Wisp

![](_static/wisp.png)

#### Weaknesses:
- ```DamageType.cold```
- ```DamageType.force```
- ```DamageType.sonic```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 23500  | 160    | 200        |
+-------+--------+--------+------------+
| 2     | 36555  | 195    | 350        |
+-------+--------+--------+------------+
| 3     | 49611  | 231    | 500        |
+-------+--------+--------+------------+
| 4     | 62666  | 266    | 650        |
+-------+--------+--------+------------+
| 5     | 75722  | 302    | 800        |
+-------+--------+--------+------------+
| 6     | 88777  | 362    | 950        |
+-------+--------+--------+------------+
| 7     | 101833 | 373    | 1100       |
+-------+--------+--------+------------+
| 8     | 114888 | 408    | 1250       |
+-------+--------+--------+------------+
| 9     | 127944 | 444    | 1400       |
+-------+--------+--------+------------+
| 10    | 141000 | 480    | 1550       |
+-------+--------+--------+------------+
```

#### Attack Logic

### Beholder

![](_static/beholder.png)

#### Weaknesses:
- ```DamageType.acid```
- ```DamageType.cold```
- ```DamageType.fire```
- ```DamageType.piercing```
- ```DamageType.slashing```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 25000  | 189    | 200        |
+-------+--------+--------+------------+
| 2     | 38888  | 228    | 350        |
+-------+--------+--------+------------+
| 3     | 52777  | 267    | 500        |
+-------+--------+--------+------------+
| 4     | 66666  | 306    | 650        |
+-------+--------+--------+------------+
| 5     | 80555  | 345    | 800        |
+-------+--------+--------+------------+
| 6     | 94444  | 384    | 950        |
+-------+--------+--------+------------+
| 7     | 108333 | 423    | 1100       |
+-------+--------+--------+------------+
| 8     | 122222 | 462    | 1250       |
+-------+--------+--------+------------+
| 9     | 136111 | 501    | 1400       |
+-------+--------+--------+------------+
| 10    | 150000 | 540    | 1550       |
+-------+--------+--------+------------+
```

#### Attack Logic

### Dragon

![](_static/dragon.png)

#### Weaknesses:
- ```DamageType.acid```
- ```DamageType.electricity```
- ```DamageType.piercing```
- ```DamageType.precision```
- ```DamageType.sonic```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 15000  | 185    | 200        |
+-------+--------+--------+------------+
| 2     | 16666  | 226    | 350        |
+-------+--------+--------+------------+
| 3     | 18333  | 267    | 500        |
+-------+--------+--------+------------+
| 4     | 20000  | 308    | 650        |
+-------+--------+--------+------------+
| 5     | 21666  | 349    | 800        |
+-------+--------+--------+------------+
| 6     | 23333  | 390    | 950        |
+-------+--------+--------+------------+
| 7     | 25000  | 431    | 1100       |
+-------+--------+--------+------------+
| 8     | 26666  | 472    | 1250       |
+-------+--------+--------+------------+
| 9     | 28333  | 513    | 1400       |
+-------+--------+--------+------------+
| 10    | 30000  | 555    | 1550       |
+-------+--------+--------+------------+
```

#### Attack Logic

### Minotaur

![](_static/minotaur.png)

#### Weaknesses:
- ```DamageType.cold```
- ```DamageType.electricity```
- ```DamageType.precision```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 28000  | 200    | 200        |
+-------+--------+--------+------------+
| 2     | 43555  | 244    | 350        |
+-------+--------+--------+------------+
| 3     | 59111  | 288    | 500        |
+-------+--------+--------+------------+
| 4     | 74666  | 333    | 650        |
+-------+--------+--------+------------+
| 5     | 90222  | 377    | 800        |
+-------+--------+--------+------------+
| 6     | 105777 | 422    | 950        |
+-------+--------+--------+------------+
| 7     | 121333 | 466    | 1100       |
+-------+--------+--------+------------+
| 8     | 136888 | 511    | 1250       |
+-------+--------+--------+------------+
| 9     | 152444 | 555    | 1400       |
+-------+--------+--------+------------+
| 10    | 168000 | 600    | 1550       |
+-------+--------+--------+------------+
```

#### Attack Logic

### Slime

![](_static/slime.png)

#### Weaknesses:
- ```DamageType.electricity```
- ```DamageType.precision```
- ```DamageType.sonic```

##### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 11000  | 150    | 235        |
+-------+--------+--------+------------+
| 2     | 12222  | 183    | 340        |
+-------+--------+--------+------------+
| 3     | 13444  | 216    | 446        |
+-------+--------+--------+------------+
| 4     | 14666  | 250    | 552        |
+-------+--------+--------+------------+
| 5     | 15888  | 283    | 658        |
+-------+--------+--------+------------+
| 6     | 17111  | 316    | 763        |
+-------+--------+--------+------------+
| 7     | 18333  | 350    | 875        |
+-------+--------+--------+------------+
| 8     | 19555  | 383    | 975        |
+-------+--------+--------+------------+
| 9     | 20777  | 416    | 1081       |
+-------+--------+--------+------------+
| 10    | 22000  | 450    | 1186       |
+-------+--------+--------+------------+
```

#### Attack Logic

### Vampire
![](_static/vampire.png)

#### Weaknesses:
- ```DamageType.fire```
- ```DamageType.piercing```
- ```DamageType.precision```
- ```DamageType.slashing```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 14025  | 175    | 200        |
+-------+--------+--------+------------+
| 2     | 27913  | 213    | 350        |
+-------+--------+--------+------------+
| 3     | 41802  | 252    | 500        |
+-------+--------+--------+------------+
| 4     | 55691  | 291    | 650        |
+-------+--------+--------+------------+
| 5     | 69580  | 330    | 800        |
+-------+--------+--------+------------+
| 6     | 83469  | 369    | 950        |
+-------+--------+--------+------------+
| 7     | 97358  | 408    | 1100       |
+-------+--------+--------+------------+
| 8     | 111247 | 447    | 1250       |
+-------+--------+--------+------------+
| 9     | 125136 | 486    | 1400       |
+-------+--------+--------+------------+
| 10    | 139025 | 525    | 1550       |
+-------+--------+--------+------------+
```

#### Attack Logic
Attacks a random player unit.


### Wraith

![](_static/wraith.png)

#### Weaknesses:
- ```DamageType.acid```
- ```DamageType.bludgeoning```
- ```DamageType.fire```
- ```DamageType.slashing```

#### Stats
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 26000  | 165    |  200       |
+-------+--------+--------+------------+
| 2     | 40444  | 201    |  350       |
+-------+--------+--------+------------+
| 3     | 54888  | 238    |  500       |
+-------+--------+--------+------------+
| 4     | 69333  | 275    |  650       |
+-------+--------+--------+------------+
| 5     | 83777  | 311    |  800       |
+-------+--------+--------+------------+
| 6     | 98222  | 348    |  950       |
+-------+--------+--------+------------+
| 7     | 112666 | 385    |  1100      |
+-------+--------+--------+------------+
| 8     | 127111 | 421    |  1250      |
+-------+--------+--------+------------+
| 9     | 141555 | 458    |  1400      |
+-------+--------+--------+------------+
| 10    | 156000 | 495    |  1550      |
+-------+--------+--------+------------+
```

#### Attack Logic
