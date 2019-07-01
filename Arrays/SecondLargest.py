def secondLargestElem(arr):
    largest = arr[0]
    secondLargest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]

        elif arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [ 14, 46, 47, 86, 92, 52, 48, 36, 66, 85 ]
    print(secondLargestElem(arr))


