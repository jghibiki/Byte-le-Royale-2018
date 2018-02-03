<img src="_static/dd.png"/> 

# Dungeon Delvers Overview

## The Event
Lead your fearless adventurers into the depths of the earth with the magical language of Python. Gather gold, fame, and glory to become the envy of your fellow competitors. 

Once the event starts, you will have 24 hours to build the best team. Never forget though, sleep is essential to successful adventuring. Get plenty of sleep! 

## The Goal

The goal is to collect more trophies than any other party of adventurers. Your task is to program the most capable party of adventurers who will traverse randomly generated dungeons to earn as many trophies as possible. Gold and trophies are awarded for killing [monsters](#monsters) but beware - monsters can be very deadly. The more dangerous a monster the more gold will be rewarded. Gold can be spent in [town](#towns) to purchase better weapons and spells for your party. [Traps](#traps), while still dangerous, allow your party to avoid monsters that are too challenging.


## The Basics

Controlling your adventurers will be as simple as using a basic Python API, which will command your units to take various actions. 

The game is made up of several phases. These phases are best described as different rooms or locations. The first location your team will visit each game is a Town (for more about towns see [Towns](#towns) and [Purchasing Items](~documentation/items.html#purchasing-items)). Once you are done in town, your party will venture out into various dungeons. A dungeon is made up of many rooms. Clearing a dungeon will allow you to return to town whereupon your team will be fully rested and healed. These dungeons will be of increasing length and difficulty so you will need to carefully plan how to survive. Once you clear a room in a dungeon you will be allowed a sneak-peek at what lies beyond. If there are two doors, you will be given the choice of which door to enter (see [Choosing Your Path](#choosing-your-path)).


The following code, is an example of a bare-bones client. A client is made up of several methods which will be called automatically by the networking mechanisms of the client which are implemented by inheriting the UserClient super-class. At the beginning of each method, there is a description of what each event-handling method does.

*Note: Tampering with any variables or methods defined by the UserClient method will be considered cheating and you will be disqualified.*


```python
import random

from game.client.user_client import UserClient
from game.common.enums import *

class CustomClient(UserClient):

    def __init__(self):
        """ 
        Use the constructor to initialize any variables you 
        would like to track between turns. 
        """
        pass

    def team_name(self):
        """
        Allows teams to set the team name. This is called once per game. 
        The character limit is 35 characters.
        """
        return "Team Coffee!"

    def unit_choice(self):
        """
        Allows teams to name their units and pick what class each unit should be.
        Only one unit of each class is allowed. Exactly four units are required.
        
        Valid Unit Types:
            - UnitClass.knight
            - UnitClass.brawler
            - UnitClass.pikeman
            - UnitClass.rogue
            - UnitClass.magus
            - UnitClass.sorcerer
            - UnitClass.wizard
            - UnitClass.alchemist 
        """
        return [
                {
                    "name": "Martin",
                    "class": UnitClass.wizard
                },
                {
                    "name": "Steve",
                    "class": UnitClass.brawler
                },
                {
                    "name": "Alphonse",
                    "class": UnitClass.rogue
                },
                {
                    "name": "Thomas",
                    "class": UnitClass.alchemist
                }
            ]


    def town(self, units, gold, store):
        """
        Allows units to purchase items while in town. Called when units 
        enter town. 
        
        In the provided example, the code print a summary of the party's current 
        gold. Then depending on if this is the first (or zero-th town) the 
        party has been to it will attempt to purchase three items for Thomas, 
        armor (to increase Thomas's health), a Fire Bomb which is placed in
        his second item slot, and an Acid Bomb which is placed in his first
        item slot. Thomas is an alchemist, alchemists have to item slots and the
        ability to purchase bombs.
        
        At the second town, Thomas purchases some upgrades/refills, and Martin
        purchases a better sword.
        
        For item properties and further documentation on how 
        to purchase items see: http://royale.ndacm.org/~documentation/items.html 
        
        Note: If the team does not have enough gold to cover the cost of an item,
        the purchase will be canceled.
        """
        print()
        print("*"*50)
        print("Town")
        print("*"*50)

        print("Gold: {}".format(gold))


        if store.get_town_number() is 0:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.armor, 1)
                store.purchase(unit, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit, ItemType.acid_bomb, 1, item_slot=1)

        elif store.get_town_number() is 1:
            unit = self.get_unit("thomas", units)
            if unit is not None:
                store.purchase(unit, ItemType.armor, 2)
                store.purchase(unit, ItemType.fire_bomb, 2, item_slot=2)
                store.purchase(unit, ItemType.fire_bomb, 2, item_slot=2)

            unit = self.get_unit("martin", units)
            if unit is not None:
                store.purchase(unit, ItemType.sword, 2)


    def room_choice(self, units, options):
    """
    When leaving a room, you will be given the opportunity to choose 
    what room you enter next. Some rooms will only have one door,
    others will have two. Options is a dictionary of your options.
        - options[Direction.right] provides access to the room on the right
        - options[Direction.left] provides access to the room on the left
        
    The room objects will have a property to determine what type of room it is.
    If:
        - room.node_type == NodeType.town: Then the room is a town
        - room.node_type == NodeType.monster: Then the room is a monster room.
            - The monster from the monster room can be found with room.monster
            - For monster properties see http://royale.ndacm.org/~documentation/monsters.html
        - room.node_type == NodeType.trap: Then the room is a trap room.
            - The trap from the trap room can be found with room.trap
            - For trap properties see http://royale.ndacm.org/~documentation/traps.html
    """

        if len(options) == 1:
            return Direction.forward

        elif len(options) == 2:
            return random.choice([Direction.right, Direction.left])

        else:
            return MessageType.null

    def combat_round(self, monster, units):
        """
        Event handler for combat. This method is called once for each round of combat. 
        If combat has ended, the room_choice method will be called.
        
        This example implementation, begins by printing a summary of the monster's stats
        and each of the party's stats. Then for each unit, if the unit (Thomas) is an
        alchemist, and Thomas has bombs in bomb slot #2, then use a bomb. If there are
        no bombs, use the alchemist resupply ability (passing the bomb slot containing the
        bomb type the alchemist would like to resupply). If the unit is not an alchemist,
        then they are told to do a basic attack.
        """
        print()
        print("*"*50)
        print("Combat")
        print("*"*50)
        print(monster.summary())
        for u in units:
            print(u.summary())

        for u in units:
            if u.unit_class == UnitClass.alchemist:
                if u.bomb_2_quantity > 0:
                    u.use_bomb_2()
                else:
                    u.resupply(2)
            else:
                u.attack()

    def trap_round(self, trap, units):
        """
        Event handler for trap avoidance. This method is called once for each round 
        while attempting to avoid a trap. Once the team has cleared the trap, the
        room_choice method will be called.
        
        This sample code begins by printing a summary of the current trap, and the
        party's stats. Then for each unit, the code selects a random trap evasion
        action. Note that using any sort of randomness is not recommended when
        competing as it will produce wildly varying performance.
        """
        print()
        print("*"*50)
        print("Trap!")
        print("*"*50)
        print(trap.summary())
        for u in units:
            print(u.summary())

        for u in units:
            u.trap_action = random.choice([
                TrapAction.little_effort, 
                TrapAction.large_effort, 
                TrapAction.evade
            ])


    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):    
        """
        A helper method to aid in retrieving a unit by name
        """
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None

```


## [Towns and Items](items.md)
In towns units are allowed to purchase new weapons, spells and armor if they have enough gold. The first room your units will be able to enter each game is town #0. At each town the availability of items is dependent on what number the town is. For example in town #0 you will be able to purchase level 2 weapons and level 1 spells and bombs.

## [Monsters](monsters.md)
Monsters are the primary obstacle you will face on your run. The slavering hordes would love nothing better than to have your units for dinner, so be prepared to fight valiantly. Every monster has its own attack preferences, strengths, and weaknesses. Only by exploiting these weaknesses will you truly show this crass menagerie who's boss.

## [Traps](traps.md)
Traps are the other hazard that you will have to contend with on your run. Traps will take a certain amount of effort to get past, with some hurting you every turn, and some killing you outright if you're not quick enough. This effort comes from a unit's Willpower or Focus, depending on the type of trap.

## Choosing your path
Your party will be faced with either one or two doors when you complete a room. If there is one, the only way you can go is forward. If there are two, you can go right or left. 

## Judging
Judging will be based on the average number of trophies earned over a large amount of runs through differing maps. You can get a good feel for how your team is doing by uploading your client to our scrimmage server, and seeing where you come out on the leaderboards. 

## Bugs and Questions
If you find a particularly exquisite feature, we would greatly appreciate you reporting it, either in person or, more preferably, by submitting an issue on our Github repo, which can be found [here](https://github.com/jghibiki/Byte-le-Royale-2018/issues). which can be found at . If you have any other questions, feel free to consult this site, or ask any of the event organizers.