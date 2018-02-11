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

Attacking a monster using a weapon, spell, or bomb with a matching weakness will deal 25% extra damage per weakness to the monster.

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
| 1     | 23500  | 160    | 50         |
+-------+--------+--------+------------+
| 2     | 36555  | 195    | 232        |
+-------+--------+--------+------------+
| 3     | 49611  | 231    | 415        |
+-------+--------+--------+------------+
| 4     | 62666  | 266    | 597        |
+-------+--------+--------+------------+
| 5     | 75722  | 302    | 779        |
+-------+--------+--------+------------+
| 6     | 88777  | 362    | 962        |
+-------+--------+--------+------------+
| 7     | 101833 | 373    | 1144       |
+-------+--------+--------+------------+
| 8     | 114888 | 408    | 1327       |
+-------+--------+--------+------------+
| 9     | 127944 | 444    | 1509       |
+-------+--------+--------+------------+
| 10    | 141000 | 480    | 1692       |
+-------+--------+--------+------------+
```

#### Attack Logic
Let me ignite the spark of your heart (and the rest of your body), and your flames will burn bright!
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
| 1     | 25000  | 189    | 87         |
+-------+--------+--------+------------+
| 2     | 38888  | 228    | 300        |
+-------+--------+--------+------------+
| 3     | 52777  | 267    | 512        |
+-------+--------+--------+------------+
| 4     | 66666  | 306    | 725        |
+-------+--------+--------+------------+
| 5     | 80555  | 345    | 986        |
+-------+--------+--------+------------+
| 6     | 94444  | 384    | 1150       |
+-------+--------+--------+------------+
| 7     | 108333 | 423    | 1362       |
+-------+--------+--------+------------+
| 8     | 122222 | 462    | 1575       |
+-------+--------+--------+------------+
| 9     | 136111 | 501    | 1787       |
+-------+--------+--------+------------+
| 10    | 150000 | 540    | 2000       |
+-------+--------+--------+------------+
```

#### Attack Logic
Beauty is in the 👁 of the Beholder, but to him, all are ugly. Quite frankly, even 👁 have no idea.

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
| 1     | 30000  | 185    | 113        |
+-------+--------+--------+------------+
| 2     | 46666  | 226    | 378        |
+-------+--------+--------+------------+
| 3     | 63333  | 267    | 643        |
+-------+--------+--------+------------+
| 4     | 80000  | 308    | 908        |
+-------+--------+--------+------------+
| 5     | 96666  | 349    | 1173       |
+-------+--------+--------+------------+
| 6     | 113333 | 390    | 1438       |
+-------+--------+--------+------------+
| 7     | 130000 | 431    | 1702       |
+-------+--------+--------+------------+
| 8     | 146666 | 472    | 1967       |
+-------+--------+--------+------------+
| 9     | 163333 | 513    | 2232       |
+-------+--------+--------+------------+
| 10    | 180000 | 555    | 2497       |
+-------+--------+--------+------------+
```

#### Attack Logic
Dragons hate those arrogant, lazy knights.

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
| 1     | 28000  | 200    | 100        |
+-------+--------+--------+------------+
| 2     | 43555  | 244    | 336        |
+-------+--------+--------+------------+
| 3     | 59111  | 288    | 572        |
+-------+--------+--------+------------+
| 4     | 74666  | 333    | 808        |
+-------+--------+--------+------------+
| 5     | 90222  | 377    | 1044       |
+-------+--------+--------+------------+
| 6     | 105777 | 422    | 1280       |
+-------+--------+--------+------------+
| 7     | 121333 | 466    | 1516       |
+-------+--------+--------+------------+
| 8     | 136888 | 511    | 1752       |
+-------+--------+--------+------------+
| 9     | 152444 | 555    | 1988       |
+-------+--------+--------+------------+
| 10    | 168000 | 600    | 2225       |
+-------+--------+--------+------------+
```

#### Attack Logic
I'd rather not get physical this time, but I'll take a swing at it!

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
| 1     | 22000  | 150    | 50         |
+-------+--------+--------+------------+
| 2     | 34222  | 183    | 209        |
+-------+--------+--------+------------+
| 3     | 46444  | 216    | 368        |
+-------+--------+--------+------------+
| 4     | 58666  | 250    | 528        |
+-------+--------+--------+------------+
| 5     | 70888  | 283    | 687        |
+-------+--------+--------+------------+
| 6     | 83111  | 316    | 847        |
+-------+--------+--------+------------+
| 7     | 95333  | 350    | 1006       |
+-------+--------+--------+------------+
| 8     | 107555 | 383    | 1166       |
+-------+--------+--------+------------+
| 9     | 119777 | 416    | 1325       |
+-------+--------+--------+------------+
| 10    | 132000 | 450    | 1485       |
+-------+--------+--------+------------+
```

#### Attack Logic
*splosh* *slorp* *slurmp* *sound of gelatin gelatinning*

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
| 1     | 25000  | 175    | 75         |
+-------+--------+--------+------------+
| 2     | 38888  | 213    | 281        |
+-------+--------+--------+------------+
| 3     | 52777  | 252    | 487        |
+-------+--------+--------+------------+
| 4     | 66666  | 291    | 693        |
+-------+--------+--------+------------+
| 5     | 80555  | 330    | 899        |
+-------+--------+--------+------------+
| 6     | 94444  | 369    | 1105       |
+-------+--------+--------+------------+
| 7     | 108333 | 408    | 1312       |
+-------+--------+--------+------------+
| 8     | 122222 | 447    | 1518       |
+-------+--------+--------+------------+
| 9     | 136111 | 486    | 1724       |
+-------+--------+--------+------------+
| 10    | 150000 | 525    | 1930       |
+-------+--------+--------+------------+
```

#### Attack Logic
What is a man? *tosses wine glass aside* A miserable pile of armor and nothing more! But enough talk! Have at you!

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
| 1     | 26000  | 165    |  62        |
+-------+--------+--------+------------+
| 2     | 40444  | 201    |  208       |
+-------+--------+--------+------------+
| 3     | 54888  | 238    |  454       |
+-------+--------+--------+------------+
| 4     | 69333  | 275    |  649       |
+-------+--------+--------+------------+
| 5     | 83777  | 311    |  845       |
+-------+--------+--------+------------+
| 6     | 98222  | 348    |  1041      |
+-------+--------+--------+------------+
| 7     | 112666 | 385    |  1237      |
+-------+--------+--------+------------+
| 8     | 127111 | 421    |  1432      |
+-------+--------+--------+------------+
| 9     | 141555 | 458    |  1628      |
+-------+--------+--------+------------+
| 10    | 156000 | 495    |  1824      |
+-------+--------+--------+------------+
```

#### Attack Logic
Allow me to spell out your doom for you loud and clear!