"""What is the greatest product of four
    adjacent numbers in any direction
    (up, down, left, right, or diagonally)
    in the 2020 grid?"""

import math



def divisors(num):
    factors = [1, num]
    for i in range(2, int(math.sqrt(num))+ 1):
        if not num % i:
            factors.append(i)
            factors.append(num / i)
    return list(set(factors))

def first_triangle_with_divisors(num):
    '''
    Find the first triangle number with
    at least num number of divisors
    '''
    count = 1
    triangle = 1
    factor_count = 0
    while factor_count < num:
        count += 1
        triangle += count
        factor_count = len(divisors(triangle))
    return (triangle, factor_count)

def main():
    """docstring for main"""
    print(first_triangle_with_divisors(500))
        
if __name__ == "__main__":
    main()
