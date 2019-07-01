## Largest Elem in array

def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max

if __name__ == "__main__":
    arr = [ 75, 29, 80, 100, 45, 60, 99, 50]
    LargestElem = largest(arr)
    print('Largest Elem: {}'.format(LargestElem))