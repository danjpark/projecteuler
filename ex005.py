""" What is the smallest positive
    number that is evenly divisible
    by all of the numbers from 1 to 20?"""
import datetime

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def listlcm(listOfNumbers):
    if len(listOfNumbers) == 2:
        return lcm(listOfNumbers[0], listOfNumbers[1])
    else:
        return lcm(listOfNumbers[0], listlcm(listOfNumbers[1:]))
       
    
def main():
    """docstring for main"""
    print(listlcm([i for i in range(1, 21)]))

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print("Total Time: "
          + str((end_time - start_time).total_seconds())
          + " seconds.")
