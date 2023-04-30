def spiralTraverse(array):
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
