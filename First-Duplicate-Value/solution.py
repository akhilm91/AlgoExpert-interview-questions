def firstDuplicateValue(array):
    array_set = set()
    for i in range(len(array)):
        if array[i] in array_set:
            return array[i]
        array_set.add(array[i])
    return -1
    
    