def find(array: list, value) -> int:
    if len(array) != 0:
        mid = len(array) // 2
        if array[mid] == value:
            return value
        return (find(array[:mid], value) if value < array[mid] else find(array[mid+1:], value))
    return -1