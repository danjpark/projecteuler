"""
    Let d(n) be defined as the sum of proper
    divisors of n (numbers less than n which
    divide evenly into n).

    If d(a) = b and d(b) = a, where a  b,
    then a and b are an amicable pair and
    each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284
    are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def sumofdivisors(x):
    sumDivisors = 0
    for i in range(1, x):
        if x % i == 0: sumDivisors += i
    return sumDivisors

def isAmicable(x):

    y = sumofdivisors(x)
    if x == sumofdivisors(y) and y == sumofdivisors(x) and x != y:
        return(x, y)
    else: return 0

def main():
    """docstring for main"""
    finalList = []
    for i in range(1, 10001):
        amicables = isAmicable(i)
        if amicables != 0 and amicables[1] not in finalList:
            finalList.append(amicables[0])
            finalList.append(amicables[1])

    print(finalList)
            
if __name__ == "__main__":
    main()
