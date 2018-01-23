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

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/wisp.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     |        |        |            |
+-------+--------+--------+------------+
| 2     |        |        |            |
+-------+--------+--------+------------+
| 3     |        |        |            |
+-------+--------+--------+------------+
| 4     |        |        |            |
+-------+--------+--------+------------+
| 5     |        |        |            |
+-------+--------+--------+------------+
| 6     |        |        |            |
+-------+--------+--------+------------+
| 7     |        |        |            |
+-------+--------+--------+------------+
| 8     |        |        |            |
+-------+--------+--------+------------+
| 9     |        |        |            |
+-------+--------+--------+------------+
| 10    |        |        |            |
+-------+--------+--------+------------+
```


**Attack Logic:**

### Beholder

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/beholder.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     |        |        |            |
+-------+--------+--------+------------+
| 2     |        |        |            |
+-------+--------+--------+------------+
| 3     |        |        |            |
+-------+--------+--------+------------+
| 4     |        |        |            |
+-------+--------+--------+------------+
| 5     |        |        |            |
+-------+--------+--------+------------+
| 6     |        |        |            |
+-------+--------+--------+------------+
| 7     |        |        |            |
+-------+--------+--------+------------+
| 8     |        |        |            |
+-------+--------+--------+------------+
| 9     |        |        |            |
+-------+--------+--------+------------+
| 10    |        |        |            |
+-------+--------+--------+------------+
```

**Attack Logic:**

### Dragon

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/dragon.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     |        |        |            |
+-------+--------+--------+------------+
| 2     |        |        |            |
+-------+--------+--------+------------+
| 3     |        |        |            |
+-------+--------+--------+------------+
| 4     |        |        |            |
+-------+--------+--------+------------+
| 5     |        |        |            |
+-------+--------+--------+------------+
| 6     |        |        |            |
+-------+--------+--------+------------+
| 7     |        |        |            |
+-------+--------+--------+------------+
| 8     |        |        |            |
+-------+--------+--------+------------+
| 9     |        |        |            |
+-------+--------+--------+------------+
| 10    |        |        |            |
+-------+--------+--------+------------+
```

**Attack Logic:**

### Minotaur

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/minotaur.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     |        |        |            |
+-------+--------+--------+------------+
| 2     |        |        |            |
+-------+--------+--------+------------+
| 3     |        |        |            |
+-------+--------+--------+------------+
| 4     |        |        |            |
+-------+--------+--------+------------+
| 5     |        |        |            |
+-------+--------+--------+------------+
| 6     |        |        |            |
+-------+--------+--------+------------+
| 7     |        |        |            |
+-------+--------+--------+------------+
| 8     |        |        |            |
+-------+--------+--------+------------+
| 9     |        |        |            |
+-------+--------+--------+------------+
| 10    |        |        |            |
+-------+--------+--------+------------+
```

**Attack Logic:**

### Slime

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/slime.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 5500   | 175    | 235        |
+-------+--------+--------+------------+
| 2     | 7425   | 271    | 340        |
+-------+--------+--------+------------+
| 3     | 9350   | 367    | 446        |
+-------+--------+--------+------------+
| 4     | 11274  | 463    | 552        |
+-------+--------+--------+------------+
| 5     | 13200  | 560    | 658        |
+-------+--------+--------+------------+
| 6     | 15125  | 656    | 763        |
+-------+--------+--------+------------+
| 7     | 17049  | 752    | 875        |
+-------+--------+--------+------------+
| 8     | 18975  | 848    | 975        |
+-------+--------+--------+------------+
| 9     | 20900  | 945    | 1081       |
+-------+--------+--------+------------+
| 10    | 22825  | 1041   | 1186       |
+-------+--------+--------+------------+
```

**Attack Logic:** 

### Goblin

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     |        |        |            |
+-------+--------+--------+------------+
| 2     |        |        |            |
+-------+--------+--------+------------+
| 3     |        |        |            |
+-------+--------+--------+------------+
| 4     |        |        |            |
+-------+--------+--------+------------+
| 5     |        |        |            |
+-------+--------+--------+------------+
| 6     |        |        |            |
+-------+--------+--------+------------+
| 7     |        |        |            |
+-------+--------+--------+------------+
| 8     |        |        |            |
+-------+--------+--------+------------+
| 9     |        |        |            |
+-------+--------+--------+------------+
| 10    |        |        |            |
+-------+--------+--------+------------+
```

**Attack Logic:** Attacks a random player unit.


### Wraith

![](https://github.com/jghibiki/Byte-le-Royale-2018/blob/master/game/visualizer/assets/wraith.png)

**Stats:**
```eval_rst
+-------+--------+--------+------------+
| Level | Health | Damage | Gold Value |
+=======+========+========+============+
| 1     | 6000   | 150    |  200       |
+-------+--------+--------+------------+
| 2     | 75000  | 225    |  350       |
+-------+--------+--------+------------+
| 3     | 90000  | 300    |  500       |
+-------+--------+--------+------------+
| 4     | 10500  | 375    |  650       |
+-------+--------+--------+------------+
| 5     | 12000  | 450    |  800       |
+-------+--------+--------+------------+
| 6     | 13500  | 525    |  950       |
+-------+--------+--------+------------+
| 7     | 15000  | 600    |  1100      |
+-------+--------+--------+------------+
| 8     | 16500  | 675    |  1250      |
+-------+--------+--------+------------+
| 9     | 18000  | 750    |  1400      |
+-------+--------+--------+------------+
| 10    | 19500  | 825    |  1550      |
+-------+--------+--------+------------+
```
