"""
                    PRIME NUMBER GENERATION
            
            Goal: create a prime number with k bits
            
            1. Set first and last bit of number to 1 to get an odd number
            2. Make the numbers in between randomly 1 or 0
            3. Apply Miller Rabin Test with t repetitions
               If any time a witness against primality is found
               jump back to step 1



"""
# -----------------------------------------------------------------------------
#                               IMPORTS
# -----------------------------------------------------------------------------

from random import randint
from MillerRabin import primeTest

# -----------------------------------------------------------------------------
#                   CREATE RANDOM ODD NUMBER WITH k BITS
# -----------------------------------------------------------------------------

def oddNumberGenerator(k):
    
    
    firstAndLastBit = [1]                                                # first and last bit are set to 1
    inBetweenBits = [randint(0,1) for i in range(1,k-1)]                 # bits in between are random 1's or 0's
    randomOddNumber = firstAndLastBit + inBetweenBits + firstAndLastBit  # combine them to a random Odd Integer
    
    
    string = ''.join(str(bit) for bit in randomOddNumber)                # make a string out of the list of bits
    randomOddNumber = int(string,2)                                      # and turn it into an integer with base 2
    
    
    return randomOddNumber
    
    



# -----------------------------------------------------------------------------
#                       GENERATE PRIME WITH k BITS
# -----------------------------------------------------------------------------

# creates a prime number with bits amount of bits
def PrimeGenerator(K):
    
    prime = oddNumberGenerator(K)
    
    while primeTest(prime) == False :
        prime = oddNumberGenerator(K) 
    
    return prime
    
    


print(PrimeGenerator(512))









































