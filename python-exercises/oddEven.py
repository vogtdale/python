# Ask the user for a number.
#  Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number = int(input())

if (number % 2 == 0):
    print("you picked an even")
else:
    print("you picked an odd")