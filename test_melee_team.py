import random

from game.client.user_client import UserClient
from game.common.enums import *



class CustomClient(UserClient):

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """

    def team_name(self):
        print("Sending Team Name")

        return "Team Meleecoats"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
                {
                    "name": "Meathead",
                    "class": UnitClass.knight
                },
                {
                    "name": "Krieg",
                    "class": UnitClass.brawler
                },
                {
                    "name": "Steroids",
                    "class": UnitClass.pikeman
                },
                {
                    "name": "Mallow",
                    "class": UnitClass.rogue
                }
            ]


    def town(self, units, gold, store):
        print()
        print("*"*50)
        print("Town")
        print("*"*50)

        print("Gold: {}".format(gold))


        if store.get_town_number() is 0:
            unit1 = self.get_unit("meathead", units)
            unit2 = self.get_unit("krieg", units)
            unit3 = self.get_unit("steroids", units)
            unit4 = self.get_unit("mallow", units)
            if unit4 is not None:
                store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)

        elif store.get_town_number() is 1:
            unit1 = self.get_unit("meathead", units)
            unit2 = self.get_unit("krieg", units)
            unit3 = self.get_unit("steroids", units)
            unit4 = self.get_unit("mallow", units)
            if unit1 is not None:
                store.purchase(unit1, ItemType.sword, 2)
            if unit2 is not None:
                store.purchase(unit2, ItemType.mace, 2)
            if unit3 is not None:
                store.purchase(unit3, ItemType.spear, 2)
            if unit4 is not None:
                store.purchase(unit4, ItemType.dagger, 2)
                store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)

                
        elif store.get_town_number() is 2:
            unit1 = self.get_unit("meathead", units)
            unit2 = self.get_unit("krieg", units)
            unit3 = self.get_unit("steroids", units)
            unit4 = self.get_unit("mallow", units)
            if unit1 is not None:
                store.purchase(unit1, ItemType.sword, 2)
            if unit2 is not None:
                store.purchase(unit2, ItemType.mace, 2)
            if unit3 is not None:
                store.purchase(unit3, ItemType.spear, 2)
            if unit4 is not None:
                store.purchase(unit4, ItemType.dagger, 2)
                store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)

        elif store.get_town_number() is 3:
            unit1 = self.get_unit("meathead", units)
            unit2 = self.get_unit("krieg", units)
            unit3 = self.get_unit("steroids", units)
            unit4 = self.get_unit("mallow", units)
            if unit1 is not None:
                store.purchase(unit1, ItemType.sword, 2)
            if unit2 is not None:
                store.purchase(unit2, ItemType.mace, 2)
            if unit3 is not None:
                store.purchase(unit3, ItemType.spear, 2)
            if unit4 is not None:
                store.purchase(unit4, ItemType.dagger, 2)
                store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
                store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)


    def room_choice(self, units, options):

        if len(options) == 1:
            return Direction.forward

        elif len(options) == 2:
            return random.choice([Direction.right, Direction.left])
        else:
            return MessageType.null

    def combat_round(self, monster, units):
        print()
        print("*"*50)
        print("Combat")
        print("*"*50)
        print(monster.summary())
        for u in units:
            print(u.summary())

        for u in units:
            if u.unit_class == UnitClass.rogue:
                if u.bomb_1_quantity > 0:
                    u.use_bomb_1()
                elif u.bomb_2_quantity > 0:
                    u.use_bomb_2()
                elif u.bomb_3_quantity > 0:
                    u.use_bomb_3()
                else:
                    u.attack()
                    
            elif u.unit_class == UnitClass.pikeman:
                if monster.current_health > 5000:
                    u.target_weakness()
                    print ("Targeting Weakness!")
                else:
                    u.attack()
                
            elif u.unit_class == UnitClass.knight:
                    if monster.current_health > 2000 and u.current_health > 6000:
                        u.taunt()
                    else:
                        u.attack()
            elif u.unit_class == UnitClass.brawler:
                if monster.current_health > 5000 and u.current_health > 6000:
                    u.fit_of_rage()
                    print("Getting real angry!")
                else:
                    u.attack()
            else:
                u.attack()

    def trap_round(self, trap, units):
        print()
        print("*"*50)
        print("Trap!")
        print("*"*50)
        print(trap.summary())
        for u in units:
            print(u.summary())

        for u in units:
            u.trap_action = random.choice([TrapAction.little_effort, TrapAction.large_effort, TrapAction.evade])


    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


