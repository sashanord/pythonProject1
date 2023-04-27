def simple_search(arr, key):
    """Простой поиск"""
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1

def binary_search(arr, start, end, key):
    """Бинарный поиск"""

    if start > end:
        return -1

    middle = start + (end - start) // 2

    if arr[middle] == key:
        return middle
    if arr[middle] > key:
        return binary_search(arr, start, middle - 1, key)

    return binary_search(arr, middle + 1, end, key)

def quick_sort(arr, start, end):
    """Быстрая сортировка для использования позднее для бинарного поиска"""

    if start >= end:
        return

    i = start
    j = end
    p = arr[start + (end - start) // 2]

    while i <= j:
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1

    if start < j:
        quick_sort(arr, start, j)
    if end > i:
        quick_sort(arr, i, end)