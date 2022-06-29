def merge(array1, array2):
    array, i, j, k = [0 for val in range(len(array1) + len(array2))], 0, 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array[k] = array1[i]
            i += 1
        else:
            array[k] = array2[j]
            j += 1
        k += 1
    
    for n in range(i, len(array1)):
        array[j+n] = array1[n]
    for n in range(j, len(array2)):
        array[i+n] = array2[n]
    
    return array


def mergeSort(array):
    if len(array) == 1:
        return array
        
    return merge(mergeSort(array[:len(array)//2]), mergeSort(array[len(array)//2:]))