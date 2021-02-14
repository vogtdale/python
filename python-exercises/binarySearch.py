# Write a function that takes an ordered list of 
# numbers (a list where the elements are in order from
# smallest to largest) and another number. 
# The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.

def find_target(arr, target):
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        middle_index = end_index - start_index / 2
        middle_value = arr[middle_index]

        if middle_value == target:
            return True
        elif target < middle_value:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    
    return False


a = [2,3,4,5,6,7,8,9]
b = 6
print(find_target(a, b))
    