def merge_sort(arr):
    temp = [None] * len(arr)
    sort(arr, temp, 0, len(arr)-1)
    return arr


def sort(arr, temp, low, up):
    if low == up:
        return

    mid = (low + up) // 2
    sort(arr, temp, low, mid)
    sort(arr, temp, mid+1, up)

    merge(arr, temp, low, mid, mid+1, up)
    copy(arr, temp, low, up)


def merge(arr, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1

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


def copy(arr, temp, low, up):
    for i in range(low, up+1):
        arr[i] = temp[i]


if __name__ == "__main__":
    arr = [6, 3, 1, 5, 9, 8]
    print(merge_sort(arr))
