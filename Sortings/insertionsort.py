import random


def insertionsort(array):
    for i in range(len(array)):
        value = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > value:
                array[j + 1] = array[j]
                array[j] = value


array = [random.randint(1, 1000) for i in range(1000)]

print(array)

insertionsort(array)

print(array)
