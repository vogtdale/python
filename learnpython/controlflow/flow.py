x = input("Enter name ")

if x == "dalo": 
    print("hellow {}".format(x))
elif x.upper() or x.lower() or x.capitalize() == "dalo":
    print("hellow {}".format(x.capitalize()))
else:
    print("wrong")

print()