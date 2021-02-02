def Dammier(n):
    for a in range(n):
        for b in range(n):
            if (a+b) % 2 == 0:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
n= int(input("please enter a number: "))
Dammier(n)