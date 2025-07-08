"""
                                     MILLER RABIN TEST
                
                Let n be an odd positive integer and s the highest power of 2
                dividing (n-1):
                    
                                    n-1 = d * 2**s
                with d being odd.
                
                If n is an odd composite number, a such that gcd(a,n) = 1 and 
                neither of the following two conditions hold
                    
                    1. a**d = 1 mod n         -> n|a**d - 1
                    
                    2. there exists a r in {0,1,2,...,s-1} such that
                       a**(d*2**r) = -1 mod n -> n|(a**(d*2**r) + 1)
                       
                then a is said to be a witness against the primality of n.
                
                If n is composite and we choose an appropriate a, there is
                a 1/4 chance that this a will not be a witness.
                
                If we choose a randomly t-times, we decrease the probability
                of a not being a witness and therefore increase the probability
                that n is indeed prime.
                
                Usually around t=5 repetitions is enough to have a high
                probability that n is prime.
                
                


"""

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

from math import gcd
from random import randint
from ModularExponent import fastModularExponent

# -----------------------------------------------------------------------------
#                           HIGHEST POWER OF 2
# -----------------------------------------------------------------------------

def highestPowerOf2(number):

    # repeatedly divide (number - 1) by 2 until result is odd
    # returns s as the highest power and the first odd number d
    # that pops up in the repeated division by 2
    
    d = number - 1
    s = 0
    
    while d % 2 == 0:
        d = d//2
        s += 1
        
    return s,d

# -----------------------------------------------------------------------------
#                           CREATE RANDOM BASE 
# -----------------------------------------------------------------------------

def randomBase(number):
    base = 0
    while gcd(base,number)!=1 or base ==0:
        base = randint(2,number-2)
    return base


# -----------------------------------------------------------------------------
#                        CHECK IF a IS A WITNESS
# -----------------------------------------------------------------------------


# tests if a is a witness against primality of number
def witnessTest(number, a):
    
    s,d = highestPowerOf2(number)
    
    x = fastModularExponent(a,d,number)
    
    if x == 1:
        return False 
    
    for r in range(0,s):
        exponent = d*2**r 
        x = fastModularExponent(a,exponent,number)
        if x == number - 1:
            return False

        
    return True



# -----------------------------------------------------------------------------
#                          MILLER RABIN TEST
# -----------------------------------------------------------------------------


# tests if number is composite for multiple random Bases
def MillerRabinTest(number, repetitions):
    
    listOfBases = []
    a = randomBase(number)
        
    for rep in range(repetitions):
        
        a = randomBase(number)
        
        if a not in listOfBases and witnessTest(number,a)==True:
            listOfBases.append(a)
            return True
            

            
    return False # number is not composite and most probably prime
        

# -----------------------------------------------------------------------------
#                       CHECK IF NUMBER IS PRIME
# -----------------------------------------------------------------------------


def primeTest(number):

    if MillerRabinTest(number,5) == False:
        return True
    return False













































