def SelectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


if __name__ == "__main__":
    arr = [6, 3, 1, 5, 9, 8]
    print(SelectionSort(arr))
