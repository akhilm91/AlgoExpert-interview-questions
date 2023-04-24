def isValidSubsequence(array, sequence):
    # Write your code here.
    q = sequence
    pointer = 0
    for i in array:
        if q[0] == i:
            q.pop(0)        
        if len(q) == 0:
            return True
    return False
