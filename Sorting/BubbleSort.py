def BubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == "__main__":
    arr = [6, 3, 1, 5, 9, 8]
    print(BubbleSort(arr))
