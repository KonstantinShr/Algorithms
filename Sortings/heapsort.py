import random


def heapsort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) // 2 - 1 - j // 2, -1, -1):

            if 2 * i + 2 <= len(arr) - 1 - j:
                if arr[2 * i + 1] > arr[2 * i + 2]:
                    if arr[i] < arr[2 * i + 1]:
                        arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                else:
                    if arr[i] < arr[2 * i + 2]:
                        arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
            else:

                if 2 * i + 1 <= len(arr) - 1 - j:
                    if arr[i] < arr[2 * i + 1]:
                        arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]

        arr[0], arr[len(arr) - 1 - j] = arr[len(arr) - 1 - j], arr[0]


array = [random.randint(1, 1000) for i in range(20)]

print(array)

heapsort(array)

print(array)
