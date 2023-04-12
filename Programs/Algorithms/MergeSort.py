# 归并排序

# create random number array
from random import randint
from turtle import left, right
def createRandomArray(n, mix, max):
    arr = []
    arr = [randint(mix, max) for i in range(n)]
    return arr

# merge 2 arrays
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))
    
    return result

# merge sort
def mergeSort(arr):
    import math
    if len(arr) < 2:
        return arr
    
    mid = math.floor(len(arr)/2)
    left, right = arr[0:mid], arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

def main():
    arr1 = createRandomArray(10, 0, 9)
    print(arr1)
    arr2 = mergeSort(arr1)
    print(arr2)

if __name__ == '__main__':
    main()
