import random


def selectionsort(arr):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        

array = [random.randint(1, 1000) for i in range(1000)]

print(array)

selectionsort(array)

print(array)
