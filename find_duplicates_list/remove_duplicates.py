def remove_duplicates(lst):
    #use another list and for loop to get unique items in list
    list_without_duplicates = []
    for item in lst:
        if item not in list_without_duplicates:
            list_without_duplicates.append(item)
    return list_without_duplicates


def remove_duplicates_set(lst):
    #using set to identify and gettings unique items in list is more time saving
    myset = set(lst)
    list_without_duplicates = list(myset)
    return list_without_duplicates
    


if __name__ == '__main__':
    st = "hello"
    fruits = ['apple', 'banana', 'coconut', 'apple', 'grapes', 'apple', 'orange', 'coconut']
    print(remove_duplicates(st))
    print(remove_duplicates(fruits))

    print(remove_duplicates_set(st))
    print(remove_duplicates_set(fruits))
