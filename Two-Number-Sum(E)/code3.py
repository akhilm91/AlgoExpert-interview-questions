def twoNumberSum(array, targetSum):
    diffMap = {}
    for i in array:
        diff = targetSum - i
        if diff in diffMap:
            return [diff, i]
        else:
            diffMap[i] = diff
    return []
