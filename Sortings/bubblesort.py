import random


def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]


arr = [random.randint(1, 1001) for i in range(1000)]
print(arr)
bubblesort(arr)
print(arr)
