def summation(arr):
    _sum = 0
    for i in range(len(arr)):
        _sum = _sum + arr[i]

    return _sum


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(summation(arr))
