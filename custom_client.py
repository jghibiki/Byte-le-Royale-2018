from game.client.client_logic import ClientLogic
from game.common.enums import *

class CustomClient(ClientLogic):

    def __init__(self, verbose):
        """
            Availiable Properties:

            self.started : a boolean that representing whether the game has started yet.
            self.tick_no : contains the number of ticks that have occured
        """
        super().__init__(verbose)


    def turn(self, turn_data):

        print("CLIENT TICK: {}".format(self.tick_no))

        if turn_data["message_type"] == MessageType.unit_choice:

            print("Sending Unit Choices")

            return {
                "message_type": MessageType.unit_choice,
                "units": [
                    {
                        "name": "Martin",
                        "class": UnitClass.knight
                    },
                    {
                        "name": "Steve",
                        "class": UnitClass.brawler
                    },
                    {
                        "name": "Ed",
                        "class": UnitClass.pikeman
                    },
                    {
                        "name": "Thomas",
                        "class": UnitClass.rogue
                    }
                ]
            }


        elif turn_data["message_type"] == MessageType.room_choice:

            if len(turn_data["options"]) == 1:

                return { "message_type": MessageType.room_choice, "choice": Direction.forward }

            if len(turn_data["options"]) == 2:

                return { "message_type": MessageType.room_choice, "choice": Direction.left }

            else:
                return { "message_type": MessageType.null }

        elif turn_data["message_type"] == MessageType.combat_round:
            print("COMBAT!")
            print(turn_data["monster"].summary())    
            for u in turn_data["units"]:
                print(u.summary())

            return_data = { "message_type": MessageType.combat_round, "actions": {}}

            for u in turn_data["units"]:

                # TODO: switch this process out for a method on the unit classes called take_action, which returns
                #  a boolean indicating if the action was valid or not based on the unit's current internal state.
                #  then instead of manually needing to generate the response, the intended action could be fetched
                #  automatically from the unit classes in the post_turn code.
                if CombatAction.primary_weapon in u.availiable_combat_actions:
                    return_data["actions"][u.name] = CombatAction.primary_weapon
                else:
                    return_data["actions"][u.name] = CombatAction.wait
            return return_data

        else:
            return { "message_type": MessageType.null }





