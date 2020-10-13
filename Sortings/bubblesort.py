import random


array = [random.randint(1, 1001) for i in range(1000)]

print(array)

for i in range(len(array)):
    for j in range(len(array)-1, i, -1):
        if array[j - 1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]

print(array)
