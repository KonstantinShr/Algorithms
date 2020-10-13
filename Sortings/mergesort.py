import random


def mergesort(arr, l, r):
    if l < r:
        middle = (l + r) // 2
        mergesort(arr, l, middle)
        mergesort(arr, middle + 1, r)
        merge(arr, l, r, middle)


def merge(arr, l, r, middle):
    left_copy = arr[l:middle + 1]
    right_copy = arr[middle + 1: r + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = l

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] < right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        sorted_index += 1

    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1


array = [random.randint(1, 1000) for i in range(20)]

print(array)

mergesort(array, 0, len(array) - 1)

print(array)
