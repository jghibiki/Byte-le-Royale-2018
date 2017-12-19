# Traps

-- trap description - describe how the trap portion of the game works --

## Effort Types:
- **Large Effort:** 
    - Description: The unit invests a large amount of effort in a small amount of time, at the cost of precision.
    - Energy cost: 5
    - Resulting Effort: 4
    - Additional Effects: None
- **Little Effort:** 
    - Description: The unit invests only a little effort, but taking time to avoid errors or mistakes.
    - Energy cost: 2
    - Resulting Effort: 2
    - Additional Effects: None
- **Evade:** 
    - Description: The unit attempts to avoid receiving damage from the trap.
    - Energy cost: 3
    - Resulting Effort: 0
    - Additional Effects: The unit takes 50% less damage from any trap effects for this round. 
- **Wait:** 
    - Description: The unit waits.
    - Energy cost: 0
    - Resulting Effort: 0
    - Additional Effects: None

## Trap Pass Types

- **Individual Pass:** Each unit must disarm/navigate/avoid the trap on their own to succeed. The party only moves on when all units have succeeded or died.

- **Group Effort Pass:** The effort of the entire party contributes to the disarming of one trap. The party only moves on once the trap effort gauge is filled.

- **Group Pass on One Success:** Each unit works to disarm/navigate/avoid their own trap. The party is able to move on once one unit succeeds in disarming a trap.

## Trap Types

### Spike Pit
- **Description:** A pit (or strip) of spikes. 
- **Effort Stat:** Willpower
- **Effort Required:** 30
- **Pass Type:** Individual Pass
- **Damage Type**: Random Unit
- **Frequency**: Every 1 turns.
- **Damage Amount**: 100

### Falling Ceiling
- **Description:** The ceiling begins lowering until it squishes adventurers.
- **Effort Stat:** Willpower
- **Effort Required:** 30
- **Pass Type:** Group Pass
- **Damage Type**: All Units
- **Frequency/Timer**: 3 turns
- **Damage Amount**: 999999


### Puzzle Box
- **Description:** An arcane, segmented box, glowing with odd runes. 
- **Effort Stat:** Focus 
- **Effort Required:** 30
- **Pass Type:** Group Pass
- **Damage Type**: Unit with lowest health.
- **Frequency/Timer**: 2 turns
- **Damage Amount**: 100

### Pendulum Bridge
- **Description:** A bridge, with many swinging axes between you and the exit. A leaver to disable the axes can be seen on the other side.
- **Effort Stat:** Willpower
- **Pass Type:** Group Pass on One Success
- **Damage Type**: Random unit.
- **Frequency/Timer**: every turn
- **Damage Amount**: 250

### Riddles of the Sphinx
- **Description:** A sphinx, waiting to tickle your mortal brain for eternity. Solve its riddles to escape.
- **Effort Stat:** Focus
- **Pass Type:** Group Pass on One Success
- **Damage Type**: Random unit.
- **Frequency/Timer**: every turn
- **Damage Amount**: 250


## Trap API

-- description of how to check a trap type given a trap object. --

-- description of the subset of the unit api that is useful for traps --


