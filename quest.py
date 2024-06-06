class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class ForestQuest(Quest):
    def __init__(self, name="A mystery clue", description="Reward : 150 yen and 50 experiences"):
        super().__init__(name, description)

    @staticmethod
    def dialog(player):
        choice = input("Would you like to play a quest? (Y/N) ")
        if choice.lower() == 'y':
            print("-----------------------")
            print("Quest: The Hidden Medal")
            print(
                "Description: You are in a dense forest, the sun is setting, and you feel a sense of adventure in the "
                "air.")
            print("You meet a strange object hidden in a hole.")
            while True:
                interaction_1 = input("Would you like to inspect it ? (Y/N) ")
                if interaction_1.lower() == 'y':
                    print("It's a gold medal, maybe it's valuable.")
                    interaction_2 = input("Would you like to take it ? (Y/N) ")
                    if interaction_2.lower() == 'y':
                        player.add_to_inventory("Gold Medal")
                        print("You carefully take the gold medal and put it in your inventory.")
                        interaction_3 = input(
                            "Suddenly, you hear a rustling in the bushes. Would you like to investigate? (Y/N) ")
                        if interaction_3.lower() == 'y':
                            print("You approach the bushes and see a small, injured animal. It's a fox.")
                            interaction_4 = input("Would you like to help the fox? (Y/N) ")
                            if interaction_4.lower() == 'y':
                                print(
                                    "You use some herbs from your inventory to treat the fox's wounds. The fox looks "
                                    "at you gratefully and runs away.")
                                print("You feel a sense of accomplishment and gain 5 experience points.")
                                player.experience += 5
                                break
                            else:
                                print(
                                    "You decide to leave the fox alone. It looks at you with "
                                    "sad eyes as you walk away.")
                                break
                        else:
                            print("You decide to ignore the sound and continue on your way.")
                            break
                    else:
                        print("You leave the medal where it is and continue on your way.")
                        break
                else:
                    print("You decide to leave the object alone and continue on your journey.")
                    break
        else:
            print("You decide to not embark on a quest right now.")