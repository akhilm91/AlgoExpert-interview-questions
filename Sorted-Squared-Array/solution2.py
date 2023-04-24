def sortedSquaredArray(array):
    # Write your code here.
    output = []
    for i in array:
        output.append(i**2)
    output.sort()
    return output
