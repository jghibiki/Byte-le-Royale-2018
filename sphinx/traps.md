# Traps & Avoiding Traps

## Avoiding Traps

Traps while often easier than monsters, can still pose a deadly threat to your party. To avoid traps, units must choose one of [four actions](#effort-types): ```TrapAction.large_effort```, ```TrapAction.little_effort```, ```TrapAction.evade```, ```TrapAction.wait```. Certain actions such as ```TrapAction.large_effort``` or ```TrapAction.little_effort``` will cost energy. The amount of energy each unit has to spend on actions is dependant on either their ```Unit.will``` or ```Unit.focus``` stats. Melee units specialize higher willpower, and magic units specialize in higher focus. If the ```Trap.stat``` property is ```TrapStat.will``` then the unit will use it's Willpower stat, if it is ```TrapStat.focus``` the unit will use it's Focus stat. As the unit chooses actions, the unit's ```Unit.current_will``` or ```Unit.current_focus``` will go down based on which action was chosen. Each round, the unit's focus or willpower will regenerate one point up to the unit's base focus or willpower (```Unit.focus``` or ```Unit.will```).

Depending on the [pass type](#trap-pass-types) (```Trap.pass_type```) of the trap, once your units have contributed enough effort to the trap (```Trap.current_effort == Trap.required_effort```), then your unit will have avoided/disarmed the trap and will be free to continue on their way.

If your units take too long however, based on the damage interval(```Trap.damage_interval```, the trap will deal ```Trap.damage``` according to a [damage type](#trap-damage-type)(```Trap.damage_type```).


### Effort Types:
- **Large Effort:** 
    - **Description:** The unit invests a large amount of effort in a small amount of time, at the cost of precision.
    - **Energy cost:** 5
    - **Resulting Effort:** 4
    - **Additional Effects:** None
    - **Enum Value:** ```TrapAction.large_effort```
- **Little Effort:** 
    - **Description:** The unit invests only a little effort, but taking time to avoid errors or mistakes.
    - **Energy cost:** 2
    - **Resulting Effort:** 2
    - **Additional Effects:** None
    - **Enum Value:** ```TrapAction.little_effort```
- **Evade:** 
    - **Description:** The unit attempts to avoid receiving damage from the trap.
    - **Energy cost:** 3
    - **Resulting Effort:** 0
    - **Additional Effects:** The unit takes 50% less damage from any trap effects for this round. 
    - **Enum Value:** ```TrapAction.evade```
- **Wait:** 
    - **Description:** The unit waits.
    - **Energy cost:** 0
    - **Resulting Effort:** 0
    - **Additional Effects:** None
    - **Enum Value:** ```TrapAction.wait```

### Trap Pass Types

- **Individual Pass:** Each unit must disarm/navigate/avoid the trap on their own to succeed. The party only moves on when all units have succeeded or died. Its enum value is ```TrapPassType.individual_pass```.

- **Group Effort Pass:** The effort of the entire party contributes to the disarming of one trap. The party only moves on once the trap effort gauge is filled. Its enum value is ```TrapPassType.group_pass```.

- **Group Pass on One Success:** Each unit works to disarm/navigate/avoid their own trap. The party is able to move on once one unit succeeds in disarming a trap. Its enum value is ```TrapPassType.group_pass_on_first_success```.

### Trap Damage Type

- ```TrapDamageType.random_one``` Randomly damages one unit.
- ```TrapDamageType.random_two``` Randomly damages two units.
- ```TrapDamageType.random_three``` Randomly damages three units.
- ```TrapDamageType.all``` Damages all units.
- ```TrapDamageType.lowest_health``` Damages unit with the lowest health.
- ```TrapDamageType.highest_health``` Damages unit with the highest health.

## Trap Properties

- ```Trap.type```: The type of trap you're currently up against. Corresponds to a ```TrapType``` enum value.
- ```Trap.stat```: Which stat (Focus or Willpower) is associated with this trap. Corresponds to a ```TrapStat``` enum value.
- ```Trap.required_effort```: The amount of effort needed to pass the trap.
- ```Trap.current_effort```: How much effort has been put into the trap.
- ```Trap.pass_type```: The [pass type](#trap-pass-types) of the trap. Corresponds to a ```TrapPassType``` enum value.
- ```Trap.damage_interval```: How often the trap will deal damage.
- ```Trap.damage```: How much damage the trap deals.
- ```Trap.damage_type```: How the trap decides who to damage.


## Trap Types

### Spike Pit
**Description:** A pit (or strip) of spikes. 

```eval_rst
+---------------------+-----------------+
| **Effort Stat**     | Willpower       |
+---------------------+-----------------+
| **Effort Required** | 50              |
+---------------------+-----------------+
| **Pass Type**       | Individual Pass |
+---------------------+-----------------+
| **Damage Type**     | Two Random Units|
+---------------------+-----------------+
| **Frequency/Timer** | Every 3 turns   |
+---------------------+-----------------+
| **Damage Amount**   | 200             |
+---------------------+-----------------+
```

### Eldritch Barrier
**Description:** An anomalous barrier, formed from the maddening truths of reality. 

```eval_rst
+---------------------+-------------------------------+
| **Effort Stat**     | Focus                         |
+---------------------+-------------------------------+
| **Effort Required** | 50                            |
+---------------------+-------------------------------+
| **Pass Type**       | Individual Pass               |
+---------------------+-------------------------------+
| **Damage Type**     | Random Unit                   |
+---------------------+-------------------------------+
| **Frequency/Timer** | Every 2 turns                 |
+---------------------+-------------------------------+
| **Damage Amount**   | 150                           |
+---------------------+-------------------------------+
```

### Falling Ceiling
**Description:** The ceiling begins lowering until it squishes adventurers.

```eval_rst
+---------------------+-----------------+
| **Effort Stat**     | Willpower       |
+---------------------+-----------------+
| **Effort Required** | 100             |
+---------------------+-----------------+
| **Pass Type**       | Group Pass      |
+---------------------+-----------------+
| **Damage Type**     | All Units       |
+---------------------+-----------------+
| **Frequency/Timer** | After 6 Turns   |
+---------------------+-----------------+
| **Damage Amount**   | 99999999        |
+---------------------+-----------------+
```


### Puzzle Box
**Description:** An arcane, segmented box, glowing with odd runes. 

```eval_rst
+---------------------+-------------------------------+
| **Effort Stat**     | Focus                         |
+---------------------+-------------------------------+
| **Effort Required** | 150                           |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass                    |
+---------------------+-------------------------------+
| **Damage Type**     | Unit with lowest health       |
+---------------------+-------------------------------+
| **Frequency/Timer** | 1 Turns                       |
+---------------------+-------------------------------+
| **Damage Amount**   | 100                           |
+---------------------+-------------------------------+
```

### Pendulum Bridge
**Description:** A bridge, with many swinging axes between you and the exit. A leaver to disable the axes can be seen on the other side.

```eval_rst
+---------------------+-------------------------------+
| **Effort Stat**     | Willpower                     |
+---------------------+-------------------------------+
| **Effort Required** | 50                            |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass on One Success     |
+---------------------+-------------------------------+
| **Damage Type**     | Random Unit                   |
+---------------------+-------------------------------+
| **Frequency/Timer** | Every 4 turns                 |
+---------------------+-------------------------------+
| **Damage Amount**   | 200                           |
+---------------------+-------------------------------+
```


### Riddles of the Sphinx
**Description:** A sphinx, waiting to tickle your mortal brain for eternity. Solve its riddles to escape.

```eval_rst
+---------------------+-------------------------------+
| **Effort Stat**     | Focus                         |
+---------------------+-------------------------------+
| **Effort Required** | 100                           |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass on One Success     |
+---------------------+-------------------------------+
| **Damage Type**     | Random Unit                   |
+---------------------+-------------------------------+
| **Frequency/Timer** | Every 2 turns                 |
+---------------------+-------------------------------+
| **Damage Amount**   | 100                           |
+---------------------+-------------------------------+
```


