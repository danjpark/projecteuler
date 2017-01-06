""" By considering the terms
    in the Fibonacci sequence
    whose values do not exceed four million,
    find the sum of the even-valued terms."""

class FibSeq(object):
    def __init__(self):
        self.lastTwoNumbers = [1, 1]
    def extend(self):
        nextNumber = self.lastTwoNumbers[0] + self.lastTwoNumbers[1]
        self.lastTwoNumbers = [self.lastTwoNumbers[1], nextNumber]
        return nextNumber

        
def main():
    """docstring for main"""
    totalSum = 0
    
    mySequence = FibSeq()
    nextNumber = 2
    while nextNumber < 4000000:
        """""""""""""""""""""""""""""""""""""""
        " There is off by one error here. You check nextNumber < sentinal
        " above, then increment it before checking for mod 2 and adding it. 
        " For example, compare my answer to yours for all Fib numbers below 400.
        " Yours includes 610. -RY (11-18)
        """""""""""""""""""""""""""""""""""""""
        nextNumber = mySequence.extend()
        if not (nextNumber % 2):
            totalSum += nextNumber

    print(totalSum)

if __name__ == "__main__":
    main()
