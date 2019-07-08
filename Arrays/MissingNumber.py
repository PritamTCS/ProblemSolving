def getMissingInfo(arr):
    n = len(arr)
    total = (n + 1) * (n + 1 + 1) / 2
    sum_Of_arr = sum(arr)
    missing = total - sum_Of_arr
    return missing

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    print(getMissingInfo(arr))