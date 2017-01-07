"""Find the largest prime factor of a composite number."""

import math

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def getFactors(number):
    factors = []
    for i in range(2, round(math.sqrt(number))):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    """docstring for main"""
    x = int(input("Give me a number: "))
    print(getFactors(x))

    factors = getFactors(x)

    for i in reversed(factors):
        if not isPrime(i):
            factors.remove(i)

    print(factors)
    
if __name__ == "__main__":
    main()
