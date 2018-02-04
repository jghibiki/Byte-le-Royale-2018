# Traps & Avoiding Traps

When your party comes upon a trap, they will struggle to escape said trap. How their struggle fares is influenced by the trap's type, associated stat, and pass type.

## Avoiding Traps

To successfully avoid traps, you will want to check which stat the trap relies on, either Focus or Willpower using the TrapStat enum. You may also want to check what is required to pass the trap, which can be found using the TrapPassType enum. From there, you will want to choose your action for a turn, using the TrapAction enum, which will be either putting in a large effort, little effort, evading the trap, or waiting and regenerating your required resource. 

You can also utilize other information, such as the trap's type (TrapType), how much total effort you need to pass the trap (required_effort), who the trap will attack (TrapDamageType), or how much effort you've put in thus far (current_effort). 

## Trap Properties
These statistics are properties of the Trap object.

```Trap.stat```: Check which stat (Focus or Willpower)is associated with this trap.

```Trap.required_effort```: Check the amount of effort needed to pass the trap,

```Trap.current_effort```: Check how much effort you have put into the trap.

```Trap.pass_type```: Check the pass type of the trap (detailed below).

```Trap.damage_interval```: How often the trap damages you.

```Trap.damage```: How much damage the trap does.

```Trap.damage_type```: Who the trap will attack.

Units can use this to judge the trap and the best course of action. Their available actions, used through TrapAction, are:

```large_effort```, ```little_effort```, ```evade```, and ```wait```.

The effects of these actions are detailed below.

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

- **Individual Pass:** Each unit must disarm/navigate/avoid the trap on their own to succeed. The party only moves on when all units have succeeded or died. Its enum value is ```individual_pass```.

- **Group Effort Pass:** The effort of the entire party contributes to the disarming of one trap. The party only moves on once the trap effort gauge is filled. Its enum value is ```group_pass```.

- **Group Pass on One Success:** Each unit works to disarm/navigate/avoid their own trap. The party is able to move on once one unit succeeds in disarming a trap. Its enum value is ```group_pass_on_first_success```.

## Trap Properties
These statistics are properties of the Trap object.

```Trap.type```: Check which type of trap you're currently up against.

```Trap.stat```: Check which stat (Focus or Willpower)is associated with this trap.

```Trap.required_effort```: Check the amount of effort needed to pass the trap.

```Trap.current_effort```: Check how much effort you have put into the trap.

```Trap.pass_type```: Check the pass type of the trap (detailed below).

```Trap.damage_interval```: How often the trap damages you.

```Trap.damage```: How much damage the trap does.

```Trap.damage_type```: Who the trap will attack.

## Trap Types



### Spike Pit
**Description:** A pit (or strip) of spikes. 

```eval_rst
+---------------------+-----------------+
| **Effort Stat**     | Willpower       |
+---------------------+-----------------+
| **Effort Required** | 30              |
+---------------------+-----------------+
| **Pass Type**       | Individual Pass |
+---------------------+-----------------+
| **Damage Type**     | Random Unit     |
+---------------------+-----------------+
| **Frequency/Timer** | Every 1 turns   |
+---------------------+-----------------+
| **Damage Amount**   | 100             |
+---------------------+-----------------+
```

### Falling Ceiling
**Description:** The ceiling begins lowering until it squishes adventurers.

```eval_rst
+---------------------+-----------------+
| **Effort Stat**     | Willpower       |
+---------------------+-----------------+
| **Effort Required** | 30              |
+---------------------+-----------------+
| **Pass Type**       | Group Pass      |
+---------------------+-----------------+
| **Damage Type**     | All Units       |
+---------------------+-----------------+
| **Frequency/Timer** | 3 Turns         |
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
| **Effort Required** | 30                            |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass                    |
+---------------------+-------------------------------+
| **Damage Type**     | Unit with lowest health       |
+---------------------+-------------------------------+
| **Frequency/Timer** | 2 Turns                       |
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
| **Effort Required** | 30                            |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass on One Success     |
+---------------------+-------------------------------+
| **Damage Type**     | Random Unit                   |
+---------------------+-------------------------------+
| **Frequency/Timer** | Every Turn                    |
+---------------------+-------------------------------+
| **Damage Amount**   | 250                           |
+---------------------+-------------------------------+
```


### Riddles of the Sphinx
**Description:** A sphinx, waiting to tickle your mortal brain for eternity. Solve its riddles to escape.

```eval_rst
+---------------------+-------------------------------+
| **Effort Stat**     | Focus                         |
+---------------------+-------------------------------+
| **Effort Required** | 30                            |
+---------------------+-------------------------------+
| **Pass Type**       | Group Pass on One Success     |
+---------------------+-------------------------------+
| **Damage Type**     | Random Unit                   |
+---------------------+-------------------------------+
| **Frequency/Timer** | Every Turn                    |
+---------------------+-------------------------------+
| **Damage Amount**   | 250                           |
+---------------------+-------------------------------+
```


