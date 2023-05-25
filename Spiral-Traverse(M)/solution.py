def spiralTraverse1(array):
    output = []   
    startRow, endRow, startCol, endCol = 0, len(array)-1, 0, len(array[0])-1
    noOfItems = (len(array))*(len(array[0]))
    direction = 'right'
    rowPtr, colPtr = 0, 0

    while len(output) != noOfItems:   
        item = array[rowPtr][colPtr]          
        if direction == 'right':
            if ((colPtr) < endCol):
                colPtr += 1
            else:  
                startRow, rowPtr = startRow+1, rowPtr+1
                direction = 'down'
                
        elif direction == 'down':
            if ((rowPtr) < endRow):
                rowPtr += 1
            else:
                endCol, colPtr = endCol-1, colPtr-1
                direction = 'left'

        elif direction == 'left':
            if ((colPtr) > startCol):
                colPtr -= 1
            else:
                endRow, rowPtr = endRow-1, rowPtr-1
                direction = 'up'
        
        elif direction == 'up':
            if ((rowPtr) > startRow):
                rowPtr -= 1
            else:
                startCol, colPtr = startCol+1, colPtr+1
                direction = 'right'   
    
        output.append(item)
                
    return output


def spiralTraverse2(array):
    startRow, endRow = 0, len(array)-1
    startCol, endCol = 0, len(array[0])-1
    totalItems = len(array) * len(array[0])
    result = []

    # while startRow <= endRow and startCol <= endCol:
    while True:
        if  len(result) == totalItems:
            break
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
            
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])
        
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow, endRow =  startRow + 1, endRow - 1
        startCol, endCol = startCol + 1, endCol - 1
        
    return result

