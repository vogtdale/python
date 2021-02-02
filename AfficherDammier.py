def dammier(num):
    
    for a in range(num):
        for b in range(num):
            if (a + b) %2 == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()
n= int(input("please enter a  number: "))
dammier(n)
