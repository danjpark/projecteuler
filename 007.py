""" What is the 10 001st prime number?"""

def isPrime(listOfPrimes, x):
    for i in listOfPrimes:
        if x % i == 0:
            return False
    return True

def main():
    """docstring for main"""
    listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 21
    
    while len(listOfPrimes) <= 10000:
        if isPrime(listOfPrimes, i):
            listOfPrimes.append(i)
        i += 2

    print(listOfPrimes[-1])
    print(len(listOfPrimes))

    

if __name__ == "__main__":
    main()
