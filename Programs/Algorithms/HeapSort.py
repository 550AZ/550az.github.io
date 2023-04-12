# Heap sort

# create random number array
import random
def createRandomArray(n, mix, max):
    arr = []
    arr = [random.randint(mix, max) for i in range(n)]
    return arr

import math
def buildMaxHeap(arr):
    for i in range(math.floor(len(arr)/2), -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if 