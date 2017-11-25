""" Find the sum of the digits go 100!
"""

import math

def main():
    """docstring for main"""
    print(sum(int(item) for item in str(math.factorial(100))) )
 
    
            
if __name__ == "__main__":
    main()
