def QuickSort(arr):
    sort(arr, 0, len(arr) - 1)
    return arr


def sort(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    sort(arr, start, p-1)
    sort(arr, p+1, end)


def partition(arr, low, up):
    pivot = arr[low]
    start = low + 1
    end = up

    while start <= end:
        while arr[start] < pivot and start < up:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        else:
            break

    arr[low] = arr[end]
    arr[end] = pivot
    return end


if __name__ == "__main__":
    arr = [6, 3, 1, 5, 9, 8]
    print(QuickSort(arr))
