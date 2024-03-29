def reverseArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

def recursive(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    recursive(arr, start + 1, end - 1)
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(reverseArray(arr))
    print(arr)