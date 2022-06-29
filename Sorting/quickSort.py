from random import randint

def partition(array, start, end):
    pivot = randint(start, end)
    array[end], array[pivot] = array[pivot], array[end]
    i = start
    for j in range(start, end):
        if array[j] < array [end]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i


def QSort(array, start, end):
    if start < end:
        pivotIndex = partition(array,start, end)
        QSort(array, start, pivotIndex-1)
        QSort(array, pivotIndex+1, end)

def quickSort(array):
    QSort(array, 0, len(array)-1)