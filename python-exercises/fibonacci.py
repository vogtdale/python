# Write a program that asks the user 
# how many Fibonnaci numbers to generate 
# and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence 
# to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# Fn = Fn-1 + Fn-2


def fibo(n):
        if n < 0:
            print("incorrect input")
        elif n == 0:
            return 0 
        elif n == 1 or n == 2:
            return 1
        else: 
            return fibo(n - 1) + fibo(n -2)

number = int(input())
c = []
for i in range(number):
    c.append(fibo(i))
print(c)