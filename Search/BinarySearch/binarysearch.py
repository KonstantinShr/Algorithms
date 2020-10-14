import random


def binarysearch(arr, key, l, r):
    while l <= r:
        m = (l + r) // 2
        if key == arr[m]:
            print("Key index: {}".format(m))
            return m
        elif key > arr[m]:
            l = m + 1
        elif key < arr[m]:
            r = m - 1

    print("Not found")
    return -1


array = [random.randint(1, 20) for i in range(20)]
print(array)

array.sort()
print(array)

print(binarysearch(array, 13, 0, len(array) - 1))
