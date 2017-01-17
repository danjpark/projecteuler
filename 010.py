""" What is the 10,001st prime number?"""

import math

def markFalse(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

def main():
    """docstring for main"""
    # using Sieve's Algo (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    # Assume all true for 2m primes
    total = 0
    sieve = [True] * 2000000

    for i in range(2, int(math.sqrt(len(sieve)))+1):
        if sieve[i]: markFalse(sieve, i)

    for i in range(2, len(sieve)):
        if sieve[i]: total += i

    print(total)    

if __name__ == "__main__":
    main()
