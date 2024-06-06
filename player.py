class Player:
    def __init__(self, name="Joe", profession="Recruit", experience=0, money=0):
        self.name = name
        self.health = 100
        self.profession = profession
        self.experience = experience
        self.money = money
        self.inventory = ["Boussole", "Carte", "Nourriture"]

    def show_inventory(self):
        print("Inventory:")
        if self.inventory:
            for i in self.inventory:
                print(f"- {i}")
        else:
            print("No Inventory")

    def show_money(self):
        print("my Wallet:")
        if self.money:
            print(f"{self.money} £")
        else:
            print("No Money")


    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to Inventory.")

    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        print(f"{item} has been removed from Inventory.")