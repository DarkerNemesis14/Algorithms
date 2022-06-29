def selectionSort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[minIndex], array[i] = array[i], array[minIndex]