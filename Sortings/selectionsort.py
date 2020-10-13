import random

array = [random.randint(1, 1000) for i in range(1000)]

print(array)

for i in range(len(array) - 1):
    index = i
    for j in range(i, len(array)):
        if array[j] < array[index]:
            index = j
    array[i], array[index] = array[index], array[i]

print(array)
