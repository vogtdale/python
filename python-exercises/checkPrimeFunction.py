# Ask the user for a number and determine 
# whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.)

num = int(input("Enter a number "))
a = [x for x in range(2, num) if num % x == 0]
print(a)

def prime(n):
    if num > 1:
        if len(a) == 0:
            print("prime")
        else: 
            print("not a prime")
    else: 
        print("not prime")   

prime(num)