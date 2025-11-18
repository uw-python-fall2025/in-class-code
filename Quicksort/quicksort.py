

def partition(a, low, high):
    pivot = a[low]
    left = low
    for i in range(low + 1, high + 1):
        if a[i] < pivot:
            left += 1
            tmp = a[i]
            a[i] = a[left]
            a[left] = tmp

    tmp = a[low]
    a[low] = a[left]
    a[left] = tmp
    return left

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot - 1)
        quicksort(a, pivot + 1, high)

data = [2, 3, 7, 9, 2, 4, 8, 5, 1, 6]

# pivot = partition(data, 0, len(data) - 1)
# print(f'Pivot: {pivot}')
# print(data)

quicksort(data, 0, len(data) - 1)
print(data)