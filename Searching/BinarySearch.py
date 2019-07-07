# works only on sorted array


def BinarySearch(arr, elem):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] == elem:
            return True
        elif elem > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    print(BinarySearch(arr, 50))
