"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math

def main():
    return(sum([i for i in range(2,9**5*6+1) if i == sum([int(j)**5 for j in str(i)])]))


if __name__ == "__main__":
    main()
