# Ask the user for a string and print out whether 
# this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = str(input("Enter a word "))
string.split(" ")
reversed_string = string[::-1]
print(reversed_string)

if string == reversed_string:
    print("This word is a palindrome")
else:
    print("This in not a palindrome")