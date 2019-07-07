# Merge two sorted arrays into another array


def merge_temp(arr1, arr2):
    temp = [None] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    k = 0

    while i <= len(arr1)-1 and j <= len(arr2)-1:
        if arr1[i] < arr2[j]:
            temp[k] = arr1[i]
            i += 1
            k += 1

        else:
            temp[k] = arr2[j]
            j += 1
            k += 1

    while i <= len(arr1) - 1:
        temp[k] = arr1[i]
        i += 1
        k += 1

    while j <= len(arr2) - 1:
        temp[k] = arr2[j]
        j += 1
        k += 1

    return temp

# Merge two sorted parts of an array into another array


def merge_in_place(arr, low1, up1, low2, up2):
    temp = [None] * len(arr)
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1

        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= up1:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= up2:
        temp[k] = arr[j]
        k += 1
        j += 1

    return temp


if __name__ == "__main__":
    arr1 = [10, 30, 50, 70, 90]
    arr2 = [20, 40, 60, 80, 100, 120, 130]
    print(merge_temp(arr1, arr2))

    arr = [1, 2, 4, 6,  3, 5, 6, 7, 13, 19]
    print(merge_in_place(arr, 0, 3, 4, 9))
