'''
Algorithm to convert Roman Numerals to Integer Number:
Take symbol one by one from starting from index 0: If current value of symbol is greater than or equal to the value of next symbol, 
then add this value to the running total. else subtract this value 
by adding the value of next symbol to the running total
'''

def romanToInt(string):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0

    for i, char in enumerate(string):
        if (i+1) == len(string) or roman_numerals[char] >= roman_numerals[string[i+1]]:
            result += roman_numerals[char]
        else:
            result -= roman_numerals[char]
    return result


print(romanToInt("III"))
print(romanToInt("VI"))





