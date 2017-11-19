""" Find the maximum total from
    top to bottom of the triangle below:
"""

import math


myTree = [[75],
          [95, 64],
          [17, 47, 82],
          [18, 35, 87, 10],
          [20,  4, 82, 47, 65],
          [19,  1, 23, 75,  3, 34],
          [88,  2, 77, 73,  7, 63, 67],
          [99, 65,  4, 28, 6, 16, 70, 92],
          [41, 41, 26, 56, 83, 40, 80, 70, 33],
          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
          [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
          [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
          [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
          [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
          [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


##myTree = [[3],
##          [7,4],
##          [2,4,6,],
##          [8,5,9,3]]


def findBeforeRoute(currentRow, currentIndex):
    # a recursive function tat in the end, returns a highest sum from the given index/row
    if currentRow == 0:
        return myTree[0][0]
   
    if currentIndex == 0:
        return myTree[currentRow][currentIndex] + findBeforeRoute(currentRow - 1, currentIndex)
    elif currentIndex == len(myTree[currentRow]) - 1:
        return myTree[currentRow][currentIndex] + findBeforeRoute(currentRow - 1, currentIndex - 1)
    else:
        goLeft = findBeforeRoute(currentRow - 1, currentIndex - 1)
        goRight =findBeforeRoute(currentRow - 1, currentIndex)
        return myTree[currentRow][currentIndex] + max(goLeft, goRight)
    return
    


def main():
    """docstring for main"""
    print(max(findBeforeRoute(14, i) for i in range(0, 14)))
 
    
            
if __name__ == "__main__":
    main()
