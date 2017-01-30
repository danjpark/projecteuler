"""What is the greatest product of four
    adjacent numbers in any direction
    (up, down, left, right, or diagonally)
    in the 2020 grid?"""

import math

def function(n, i):
    if n == 1: return (1, i)
    elif n % 2 == 0: return function(n / 2, i + 1)
    else: return function((3 * n) + 1, i + 1)
    

def main():
    """docstring for main"""
    finalList = {}
    for i in range(500000, 1000001):
        finalList[function(i, 1)[1]] = i

    print(finalList[max(finalList.keys())])
        
if __name__ == "__main__":
    main()
