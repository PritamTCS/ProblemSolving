def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

    return sum

arr = [ 10, 20, 30, 40, 50 ]
print(sum(arr))