# Traps & Avoiding Traps

-- trap description - describe how the trap portion of the game works --

## Avoiding Traps

-- description of how to check a trap type given a trap object. --

-- description of the subset of the unit api that is useful for traps --

### Effort Types:
- **Large Effort:** 
    - **Description:** The unit invests a large amount of effort in a small amount of time, at the cost of precision.
    - **Energy cost:** 5
    - **Resulting Effort:** 4
    - **Additional Effects:** None
- **Little Effort:** 
    - **Description:** The unit invests only a little effort, but taking time to avoid errors or mistakes.
    - **Energy cost:** 2
    - **Resulting Effort:** 2
    - **Additional Effects:** None
- **Evade:** 
    - **Description:** The unit attempts to avoid receiving damage from the trap.
    - **Energy cost:** 3
    - **Resulting Effort:** 0
    - **Additional Effects:** The unit takes 50% less damage from any trap effects for this round. 
- **Wait:** 
    - **Description:** The unit waits.
    - **Energy cost:** 0
    - **Resulting Effort:** 0
    - **Additional Effects:** None

### Trap Pass Types

- **Individual Pass:** Each unit must disarm/navigate/avoid the trap on their own to succeed. The party only moves on when all units have succeeded or died.

- **Group Effort Pass:** The effort of the entire party contributes to the disarming of one trap. The party only moves on once the trap effort gauge is filled.

- **Group Pass on One Success:** Each unit works to disarm/navigate/avoid their own trap. The party is able to move on once one unit succeeds in disarming a trap.

## General Trap Properties

General properties of traps

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


