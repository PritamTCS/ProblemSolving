
def SumPairs(arr, sum):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == sum:
                return (arr[i], arr[j])


def SumPairs1(arr, sum):
    s = set()
    for i in range(len(arr)):
        s.add(arr[i])

    for i in range(len(arr)):
        temp = sum - arr[i]
        if temp in s:
            return (temp, arr[i])


if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5, 4]
    print(SumPairs(arr, 12))
    print(SumPairs1(arr, 12))
