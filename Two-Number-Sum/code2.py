def twoNumberSum(array, targetSum):
    array.sort()
    left, right = 0, len(array)-1    
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left = left + 1
        else:
            right = right - 1 
    return []
