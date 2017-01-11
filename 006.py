""" Find the difference between
    the sum of the squares of the
    first one hundred natural numbers
    and the square of the sum."""

def main():
    """docstring for main"""
    n = 100

    sumThroughN = n * (n+1)/2
    sumOfSquares = (n**3) / 3 + (n**2) / 2 + n / 6

    print((sumThroughN ** 2) - sumOfSquares)
    

    

if __name__ == "__main__":
    main()
