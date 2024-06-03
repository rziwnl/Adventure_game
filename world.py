class World:
    def __init__(self):
        self.locations = {
            "forest": "You are high in a dense forest. Thick trees surround you.",
            "castle": "You are standing in front of a majestic castle with large wooden doors.",
            "village": "You arrive in a small, lively village with friendly locals."
        }

    def explore(self, player):
        print("Where do you want to go?")
        for location in self.locations.keys():
            print(f"- {location}")

        choice = input("Enter the location name: ").lower()
        if choice in self.locations:
            print(self.locations[choice])
        else:
            print("Invalid location. Please choose a valid location.")
