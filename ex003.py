"""Find the largest prime factor of a composite number."""

import math
import datetime

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def getFactors(number):
    factors = []
    midpoint = int(pow(number,0.5))
    for i in range(2, midpoint): #round(math.sqrt(number))):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    """docstring for main"""
    ## x = int(input("Give me a number: "))
    x = 600851475143
    
    print(getFactors(x))

    factors = getFactors(x)

    for i in reversed(factors):
        if not isPrime(i):
            factors.remove(i)

    print(factors)
    
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print("Total Time: "
          + str((end_time - start_time).total_seconds())
          + " seconds.")
