""" What is the sum of the
    digits of the number 2^1000?
"""

import math

def main():
    """docstring for main"""
    total = 0
    for i in str(2**1000):
        total += int(i)

    print(total)
   
            
if __name__ == "__main__":
    main()
