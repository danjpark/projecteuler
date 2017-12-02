"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math

def main():
    foo = set([])
    max =100
    for i in range(2,max + 1):
        for j in range(2,max + 1):
            foo.add(pow(i,j))
    print(len(foo))

            
if __name__ == "__main__":
    main()
