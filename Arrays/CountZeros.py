## Traverse through the array, and as soon as we find 0,
## return len(arr) - index of first 0

def CountZeroes(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return len(arr) - i


if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    print(CountZeroes(arr))
