def arrayOfProducts1(array):
    l = len(array)
    output, leftRightProd, rightLeftProd = l*[0], l*[0], l*[0]
    
    currentProd = 1    
    for i in range(l):
        leftRightProd[i] = currentProd
        currentProd = currentProd * array[i]

    currentProd = 1    
    for j in reversed(range(l)):
        rightLeftProd[j] = currentProd
        currentProd = currentProd * array[j]

    for k in range(l):
        output[k] = leftRightProd[k] * rightLeftProd[k]

    return output

def arrayOfProducts2(array):
    l = len(array)
    product = [1]*len(array)

    left_right_product = 1
    for i in range(l):
        product[i] = left_right_product
        left_right_product = left_right_product*array[i]

    right_left_product = 1
    for j in reversed(range(l)):        
        product[j] = product[j]*right_left_product
        right_left_product = right_left_product*array[j]

    return product