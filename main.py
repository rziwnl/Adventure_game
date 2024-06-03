from player import Player
from world import World

def main():
    print("Welcome to the world of Adventure Game!")
    name = input("What is your name? ")
    profession = input("What is your profession? ")
    player = Player(name, profession)
    world = World()

    while True:
        try:
            print("------------------------")
            print("What do you want to do? ")
            choice = input("Travel, Info, Inventory, Wallet, Quit : ")
            if choice == "Travel":
                location = world.explore(player)
                if location == "forest":
                    player.experience += 3
                elif location == "castle":
                    player.experience += 1
                elif location == "village":
                    player.experience += 0.5

            elif choice == "Info":
                print(f"Name: {player.name}, Profession: {player.profession}, Experience: {player.experience}")
            elif choice == "Inventory":
                player.show_inventory()
            elif choice == "Wallet":
                player.show_money()
            elif choice == "Quit":
                print("Thanks for playing!")
                break
            else:
                print("Answer not valid!")
        except ValueError:
            print("Name a category")


if __name__ == "__main__":
    main()