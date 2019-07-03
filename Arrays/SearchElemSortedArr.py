def FindPivot(arr):
    pivot = -1
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            pivot = i+1
            break
    return pivot


def binarySearch(arr, start, end, elem):
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        elif elem > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def pivotedBinarySearch(arr, elem):
    pivot = FindPivot(arr)
    if elem == arr[pivot]:
        return pivot
    elif elem > arr[0]:
        return binarySearch(arr, 0, pivot - 1, elem)
    else:
        return binarySearch(arr, pivot + 1, len(arr)-1, elem)


        


if __name__ == "__main__":
    arr = [ 40, 50, 60, 70, 80, 10, 20, 30]
    lst = [ x for x in range(5, 11)]
    print(FindPivot(arr))
    # print(binarySearch(lst, 6))
    print(pivotedBinarySearch(arr, 10))


