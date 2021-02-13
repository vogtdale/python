def element_search(odered_list, elemnt_to_find):
    for element in odered_list:
        if element == elemnt_to_find: 
            return True
    return False

if __name__ == "__main__":
     l = [2, 4, 6, 8, 10]

     print(element_search(l, 25))
     print(element_search(l, 4))
     print(element_search(l, 8))
