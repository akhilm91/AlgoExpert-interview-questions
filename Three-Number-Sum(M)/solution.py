def threeNumberSum(array, targetSum):
    array.sort()
    ptr, output = 0, []
    while ptr < len(array)-1:
        left, right = ptr+1, len(array)-1
        while left < right:
            current_sum = array[ptr] + array[left] + array[right]
            if current_sum == targetSum:
                output.append([array[ptr], array[left], array[right]])
                left, right = left+1, right-1
            elif current_sum > targetSum:
                right -= 1
            else:
                left += 1
        ptr += 1
    return output