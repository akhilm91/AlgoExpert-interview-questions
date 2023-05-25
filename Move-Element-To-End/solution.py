def moveElementToEnd1(array, toMove):
    left = 0
    right = len(array)-1
    while left < right:
        if (array[left]==toMove) and (array[right]!=toMove):
            array[left], array[right] = array[right], array[left]
        elif (array[left]!=toMove) and (array[right]!=toMove):
            left = left+1
        elif (array[left]!=toMove) and (array[right]==toMove):
            left, right = left+1, right-1
        elif (array[left]==toMove) and (array[right]==toMove):
            right = right-1
    return array

def moveElementToEnd2(array, toMove):
    left, right = 0, len(array)-1   
    
    # check if array is empty
    if right == -1:
        return array
        
    while array[right] == toMove:
        right -= 1 
        if right < 1:
            return array
            
    while left < right:  
        if array[left] == toMove:            
            array[left], array[right] = array[right], array[left]
            right = right-1
        else:
            left += 1
    return array

def moveElementToEnd3(array, toMove):
    for i in reversed(range(len(array))):
        if array[i] == toMove:
            array.pop(i)
            array.append(toMove)             
    return array