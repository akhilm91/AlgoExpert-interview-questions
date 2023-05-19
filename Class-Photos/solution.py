def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    blueShirtHeights.sort()
    redShirtHeights.sort()
    if blueShirtHeights[-1] > redShirtHeights[-1]:    
        for i in range(len(redShirtHeights)):
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
    else:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False        
    return True