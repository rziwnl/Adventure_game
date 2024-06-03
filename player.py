class Player:
    def __init__(self, name="Joe", profession="Recruit"):
        self.name = name
        self.health = 100
        self.profession = profession
        self.inventory = ["Boussole", "Carte", "Nourriture"]

    def show_inventory(self):
        print("Inventory:")
        if self.inventory:
            for i in self.inventory:
                print(f"- {i}")
        else:
            print("No Inventory")