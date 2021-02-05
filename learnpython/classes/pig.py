from animal import Animal

class Pig(Animal):
   def __init__(self, race, sound, color):
      super().__init__(race, sound)
      self.color = color

   def display(self):
        print("the animal is a " + self.race, "and makes a " + self.sound+" sound" + " and is " + self.color)





def Main():
        obj = Pig("chochon", "onk", "pink")
        print(obj.display())
        print()

Main()