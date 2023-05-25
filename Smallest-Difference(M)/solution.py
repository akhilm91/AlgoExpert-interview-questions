
# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is the length of the second input array
def smallestDifference1(arrayOne, arrayTwo):
    ptrOne, ptrTwo = 0, 0
    arrayOne.sort()
    arrayTwo.sort()
    output, smallest = [], float("inf")
    while ptrOne < len(arrayOne) and ptrTwo < len(arrayTwo):
        numberOne, numberTwo = arrayOne[ptrOne], arrayTwo[ptrTwo]
        currentDiff = abs(numberOne - numberTwo)
        if currentDiff < smallest:
            smallest = currentDiff
            output = [numberOne, numberTwo]
        if currentDiff == 0:
            return [numberOne, numberTwo]
        if numberOne < numberTwo:
            ptrOne += 1
        else:
            ptrTwo += 1
    return output

# brute force approach
def smallestDifference2(arrayOne, arrayTwo):    
    output, smallest = [], float("inf")
    for i in arrayOne:
        for j in arrayTwo:
            diff = abs(i-j)
            if diff == 0:
                return [i, j]
            if diff < smallest:
                smallest = diff
                output = [i, j]
    return output