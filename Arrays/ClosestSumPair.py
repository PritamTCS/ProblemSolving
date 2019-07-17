import math
def FindSumClosestSumPair(arr, sum):
    diff = math.inf
    res_left = 0
    res_right = 0
    leftIndx = 0
    rightIndx = len(arr) - 1
    while leftIndx < rightIndx:
        if abs(arr[leftIndx] + arr[rightIndx] - sum) < diff:
            res_left = leftIndx
            res_right = rightIndx
            diff = abs(arr[leftIndx] + arr[rightIndx] - sum)

        if arr[leftIndx] + arr[rightIndx] > sum:
            rightIndx -= 1

        else:
            leftIndx += 1
    return arr[res_left], arr[res_right]

if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    print(FindSumClosestSumPair(arr, 54))
        
       

