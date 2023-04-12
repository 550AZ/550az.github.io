# 实现快速排序

# create random number array
from random import randint
def createRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for i in range(n)]
    return arr

def quickSort(data):
    if len(data) < 2:
        return data

    left, right = [], []
    pivot = data.pop(0)
    for num in data:
        if num >= pivot:
            right.append(num)
        else:
            left.append(num)

    print('----------')
    print(data)
    print(left, [pivot], right)

    return quickSort(left)+[pivot]+quickSort(right)


def main():
    arr1 = createRandomArray(10, 0, 9)
    print(arr1)
    arr2 = quickSort(arr1)
    print(arr2)

if __name__ == '__main__':
    main()