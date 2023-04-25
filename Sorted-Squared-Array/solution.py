def sortedSquaredArray1(array):
    # Write your code here.
    output = []
    left, right = 0, len(array)-1
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            output.insert(0, array[right]**2)
            right = right-1            
        else:
            output.insert(0, array[left]**2)
            left = left+1 
    return output


def sortedSquaredArray2(array):
    # Write your code here.
    output = []
    for i in array:
        output.append(i**2)
    output.sort()
    return output
