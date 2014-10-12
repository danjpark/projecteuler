""" Find the largest palindrome made
    from the product of two 3-digit numbers."""
import datetime

def isPalindrome(x):
    # x is a string
    if len(x) % 2 != 0:
        #if string is even length
        for i in range(0, int(len(x)/2 - 0.5)):
            # i.e. "dasad" length is 5
            # i want to go from 0 thru 1
            # so i use length/2
            if x[i] != x[-(i+1)]:
                return False
        return True
    else:
        #if string is even length
        for i in range(0, int(len(x)/2)):
            # i.e. "daniel" length is 6
            # i want to go from 0 thru 2
            # so i use length/2
            if x[i] != x[-(i+1)]:
                return False
        return True

        
def main():
    """docstring for main"""
    productList = []

    for i in range(999, 100, -1):
        for j in range(990, 100, -11):
            if isPalindrome(str(i * j)):
                if i*j not in productList:
                    productList.append(i*j)
    productList.sort()
    print(productList)

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print("Total Time: "
          + str((end_time - start_time).total_seconds())
          + " seconds.")
