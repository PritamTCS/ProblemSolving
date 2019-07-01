def leftRotate(arr, d):
    for i in range(d):
        leftRotatebyOne(arr)


def leftRotatebyOne(arr):
        temp = arr[0]
        for i in range(len(arr)-1):
                arr[i] = arr[i + 1]
        
        arr[len(arr) - 1] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print('Original Arr: {}'.format(arr))
    leftRotate(arr, d)
    print('Reversed Arr by {} elements: {}'.format(d, arr))




        