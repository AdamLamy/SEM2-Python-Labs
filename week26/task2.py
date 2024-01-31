def getProduct(text):
    textArray = text.split('*')
    product = 1
    for num in textArray:
        product = product * int(num)

    return product


#main
text = "12*2*10"
print(getProduct(text))