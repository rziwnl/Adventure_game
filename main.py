from player import Player


def main():
    print("Welcome to the world of Adventure Game!")
    name = input("What is your name? ")
    profession = input("What is your profession? ")
    player = Player(name, profession)

    while True:
        try:
            print("What do you want to do? ")
            choice = input("Travel, Inventory, Quit : ")
            if choice == "Travel":
                pass
            elif choice == "Inventory":
                player.show_inventory()
            elif choice == "Quit":
                print("Thanks for playing!")
                break
            else:
                print("Answer not valid!")
        except ValueError:
            print("Name a category")


if __name__ == "__main__":
    main()