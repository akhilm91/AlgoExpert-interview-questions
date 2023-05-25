def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    output = 0
    redShirtSpeeds.sort()    
    if fastest:
        blueShirtSpeeds.sort(reverse=True)        
    else:
        blueShirtSpeeds.sort()
    
    for i in range(len(redShirtSpeeds)):
        output = output + max(redShirtSpeeds[i], blueShirtSpeeds[i])               
    return output
