# Exercise 14
# Write a function that asks the user for a string containing multiple words. Print
# back to the user the same string, except with the words in backwards order.

a = str(input("Enter a sentence: "))

def split_word(x):
    y = x.split()
    return " ".join(y[::-1])

print(split_word(a))