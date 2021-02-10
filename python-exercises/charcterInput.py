# Create a program that asks the user to enter 
# their name and their age. Print out a message 
# addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")
age = input("How old are you? ")
result =  str((2021 - int(age))+100)
print("{}, will be 100 years old in the year {}".format(name, result ))
print(f"{name}, will be 100 years old in the year {result}")