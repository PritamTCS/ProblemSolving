def OddOccurence(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]

if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
    print(OddOccurence(arr))
