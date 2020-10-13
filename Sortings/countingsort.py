import random


def countingsort(arr):
    sort_array = [0] * max(arr)
    for i in range(len(arr)):
        sort_array[arr[i] - 1] += 1

    k = 0
    for i in range(len(sort_array)):
        if sort_array[i] != 0:
            for j in range(sort_array[i]):
                arr[k] = i + 1
                k += 1


array = [random.randint(1, 50) for i in range(50)]

print(array)

countingsort(array)

print(array)
