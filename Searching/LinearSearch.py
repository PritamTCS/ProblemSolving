def LinearSearch(arr, elem):
    for k in arr:
        if k == elem:
            return True
    return False


def LinearSearchSortedArr(arr, elem):
    for i in range(len(arr)):
        if arr[i] >= elem:
            break
    if arr[i] == elem:
        return True
    else:
        return False


if __name__ == "__main__":
    arr = [20, 45, 8, 13, 81]
    arr_sorted = [10, 20, 30, 40]
    print(LinearSearch(arr, 13))
    print(LinearSearchSortedArr(arr_sorted, 50))
