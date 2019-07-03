## arr = [1, 2, 5, 1, 7, 2, 4, 2, 10, 11, 22]

def removeDuplicates(arr):
    my_dict = { key: 0 for key in arr}
    return my_dict.keys()

def removeDuplicates1(arr):
    my_dict = {}
    for i in arr:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict.keys()



if __name__ == "__main__":
    arr = [1, 2, 5, 1, 7, 2, 4, 2, 10, 11, 22, 22]
    print(removeDuplicates(arr))
    print(removeDuplicates1(arr))



