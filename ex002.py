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
        print(nextNumber)
        return nextNumber

        
def main():
    """docstring for main"""
    totalSum = 0
    
    mySequence = FibSeq()
    nextNumber = 2
    while nextNumber < 4000000:
        nextNumber = mySequence.extend()
        if nextNumber % 2 == 0:
            totalSum += nextNumber

    print(totalSum)

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print("Total Time: "
          + str((end_time - start_time).total_seconds())
          + " seconds.")
