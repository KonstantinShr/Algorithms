import random


def partition(arr, l, r):
    middle = arr[(l + r) // 2]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while arr[i] < middle:
            i += 1

        j -= 1
        while arr[j] > middle:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, l, r):
    if l < r:
        middle = partition(arr, l, r)
        quicksort(arr, l, middle)
        quicksort(arr, middle + 1, r)


array = [random.randint(1, 1000) for i in range(20)]

print(array)

quicksort(array, 0, len(array) - 1)

print(array)
