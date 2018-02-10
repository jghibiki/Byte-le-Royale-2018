# Choosing Your Path

Your party will be faced with either one or two doors when you complete a room. 

If there is one path (i.e. ```len(options.keys()) == 1```), the only way you can go is forward by returning (```Direction.forward```) in the (```Client.room_choice()```) method. 

```python
def room_choice(self, units, options):
    if len(options.keys()) == 1:
        # there is only one door, may as well go through it
        # the only way is forward.
        return Direction.forward
```

If there are two doors (i.e. ```len(options.keys() == 2```), you can go left or right by returning ```Direction.left``` or ```Direction.Right```. 

```python
import random

def room_choice(self, units, options):
    if len(options.keys()) == 2:
        # there are two directions we can go.
        # Let's choose a random one. 
        # **Note:** Don't ever do anything random in practice you will regret it.
        
        return random.choice([Direction.left, Direction.right])
```

You can also examine the room object with ```options[Direction.right]``` or ```options[Direction.left]``` in order to look at its properties. 

```python
def room_choice(self, units, options):
    if len(options.keys()) == 2:
        right = options[Direction.right]
        
        # the variable "right" now holds a room object.
        # Below we will discuss room objects.

```

Before you look at the properties on the room object you will first want to determine what kind of room it is, to do this you can do following:

```python
def room_choice(self, units, options):
    if len(options.keys()) == 2:
        right = options[Direction.right]
        left = options[Direction.left]
        
        if right.node_type == NodeType.monster:
            monster = right.monster
            # Reference https://royale.ndacm.org/~documentation/monsters.html#monster-properties for monster properties
        elif right.node_type == NodeType.trap:
            trap = right.trap
            # Reference https://royale.ndacm.org/~documentation/traps.html#trap-properties for trap properties.
        
```

In total there are three kinds of rooms:
- Monster Rooms
    - When you enter a monster room, the client will call ```Client.combat_round()```
- Trap Rooms
    - When you enter a trap room, the client will call ```Client.trap_round()```
- Towns
    - When you enter a town, the client will call ```Client.town()```


