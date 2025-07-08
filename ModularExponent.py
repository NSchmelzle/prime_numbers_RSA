import math


def fastModularExponent(a,b,n):
    binary_list = []
    binary_string = str(bin(b))
    for i in range(2,len(binary_string)):
        binary_list.append(binary_string[i])

    binary_list.reverse()
    
    #print(binary_list)
    
    # calculate squares
    square_list = []
    square = a
    square_list.append(a)
    for i in range(0,len(binary_list)-1):
        square = (square**2)%n
        square_list.append(square)
    
    #print(square_list)
    
    # Multiply the squares
    product = 1
    binary_squares = list(zip(binary_list,square_list))
    #print(binary_squares)
    
    for element in binary_squares:
        if element[0]=='1':
            product *= element[1]%n
    
    return product%n
