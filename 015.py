"""What is the greatest product of four
    adjacent numbers in any direction
    (up, down, left, right, or diagonally)
    in the 2020 grid?"""

import math

def factorial(x):
    if x == 0: return 1
    else: return(x * factorial(x - 1))

def main():
    """docstring for main"""
    print(factorial(40) / (factorial(20) * factorial(20)))
            
if __name__ == "__main__":
    main()
