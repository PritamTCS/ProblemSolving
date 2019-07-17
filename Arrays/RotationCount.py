def RotationCount(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_indx = i
    return min_indx

if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    print(RotationCount(arr))