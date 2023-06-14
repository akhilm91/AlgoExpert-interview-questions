#solution 1
def isMonotonic1(array):
    isIncr, isDecr = False, False
    for ptr in range(1, len(array)):
        if array[ptr] > array[ptr-1]:
            isIncr = True
        elif array[ptr] < array[ptr-1]:
            isDecr = True
        if isIncr and isDecr:
            return False
    return True 

#solution 2
def isMonotonic2(array):
    for i in range(1, len(array)):
        incr = True
        if array[i] < array[i-1]:
            incr = False
            break

    for i in range(1, len(array)):
        if incr:
            if array[i] < array[i-1]:
                return False
        else:
            if array[i] > array[i-1]:
                return False
    return True   

#solution 3
def isMonotonic3(array):
    final = False
    for i in range(1, len(array)):
        if final == False:
            if array[i] > array[i-1]:
                incr, final = True, True
            elif array[i] < array[i-1]:
                incr, final = False, True
        else:
            if incr:
                if array[i] < array[i-1]:
                    return False
            else:
                if array[i] > array[i-1]:
                    return False      
    return True