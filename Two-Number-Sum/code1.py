def twoNumberSum(array, targetSum):
    # Write your code here.
    output = []
    diff_map = {}
    diff = 0
    for i in range(len(array)):
        diff = targetSum - array[i]
        if diff in diff_map:
            output = [diff, array[i]]
        diff_map[array[i]] = i
    return output    
