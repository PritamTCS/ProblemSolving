def SortFreq(arr):
    my_dict = {}

    for k in arr:
        if k in my_dict.keys():
            my_dict[k] += 1
        else:
            my_dict[k] = 1

    arr_sorted = sorted(my_dict.values(), reverse=False)
    # print(arr_sorted)
    for i in arr_sorted:
        for k, v in my_dict.items():
            if i == v:
                for j in range(v):
                    print(k)


if __name__ == "__main__":
    arr = [2, 5, 2, 8, 2, 6, 8, 8, 5, 8]
    SortFreq(arr)