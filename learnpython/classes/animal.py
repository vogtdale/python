class Animal():
    def __init__(self, race, sound):
        self.race = race
        self.sound = sound

    def display(self):
        print("the animal is a " + self.race, "and makes a " + self.sound+" sound")