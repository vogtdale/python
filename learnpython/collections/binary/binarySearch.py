def find(arr, target):
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        middle_index = end_index - start_index // 2
        middle_value = arr[middle_index]

        if middle_value == target:
            return True
        elif target < middle_value:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return False

if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7,8]
    target = 4
    print(find(arr, target))
