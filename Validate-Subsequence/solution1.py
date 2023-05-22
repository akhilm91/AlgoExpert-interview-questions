def isValidSubsequence(array, sequence):
    q = sequence
    for i in array:
        if q[0] == i:
            q.pop(0)        
        if len(q) == 0:
            return True
    return False
