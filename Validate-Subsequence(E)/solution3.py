def isValidSubsequence(array, sequence):
    for i in range(len(array)-1, -1, -1):        
        if array[i] == sequence[-1]:
            sequence.pop()
        if len(sequence) == 0:
            return True
    return False
