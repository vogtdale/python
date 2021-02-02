def sarcus(n):
    while n != 1:
        if n % 2 == 0:
            return n // 2
        else:
            return 3*n + 1

numbers = int(input())
tab = []
for i in range(numbers):
    n=int(input())
    tab.append(n)
    print(sarcus(n))
print (tab)
    


