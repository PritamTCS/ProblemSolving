import math
def ClosestProductPair(arr, product):
    diff = math.inf
    leftIndx = 0
    res_l = 0
    res_r = 0
    rightIndx = len(arr) - 1
    while leftIndx < rightIndx:
        if abs((arr[leftIndx] * arr[rightIndx]) - product) < diff:
            res_l = leftIndx
            res_r = rightIndx
            diff = abs((arr[leftIndx] * arr[rightIndx]) - product)

        if arr[leftIndx] * arr[rightIndx] > product:
            rightIndx -= 1
        else:
            leftIndx += 1

    return arr[res_l], arr[res_r]

if __name__ == "__main__":
    arr = [2, 3, 5, 9]
    print(ClosestProductPair(arr, 8))
        
