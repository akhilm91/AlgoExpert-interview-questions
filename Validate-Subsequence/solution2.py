def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False    
    pointer = 0
    for i in array:
        if sequence[pointer] == i:
            pointer = pointer+1        
        if pointer == len(sequence):
            return True
    return False
