## arr = [ 10, 20, 30, 40, 50, 60 ]
## rotated_arr = [ 40, 50, 60, 10, 20, 30 ]


def findPivot(arr):
    pivot = -1
    if len(arr) > 0:
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                pivot = i+1
                break
    return pivot


def findPivotBinarySearch(arr):
    if (len(arr) == 0):
        return -1

    if arr[0] < arr[len(arr) - 1]:
        return 0

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + end // 2
        if arr[mid] > arr[mid+1]:
            return mid + 1

        elif arr[start] <= arr[mid]:
            start = mid + 1  # search in right half

        else:
            end = mid - 1
    return 0


if __name__ == "__main__":
    arr = [40, 50, 60, 10, 20, 30]
    print(findPivot(arr))
