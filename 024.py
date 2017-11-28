"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math

## how many are there with 0 as the first?
## there is exactly 9!
## so we can look at 1m / 9! to see what the first number will be..
## 9! = 362880
## 362880 * 2 = 725760
## so, we can see the first number would be 2
## we need the 274240th number that starts with 2

## 274240 / 8! = 6.8 ; 274240 % 8! = 32320
## so its the 6th number (0, 1, 3, 4, 5, 6, 7...)
## we need the 32320th number that starts wtih 27

## 32320 / 7! = 6.4 ; 32320 % 7! = 2080
## so its the 6th number (0, 1, 3, 4, 5, 6, 8...)
## we need the 2080th number that starts wtih 278..

## 2080 / 6! = 2.89 ; 32320 % 6! = 640
## so its the 2nd number (0, 1, 3, 4, 5, ...)
## we need the 640th number that starts wtih 2783..


## 640 / 5! = 6.4 ; 640 % 5! = 40
## so its the 6th number (0, 3, 4, 5, 8, 9)
## we need the 40th number that starts wtih 27839..

## 40 / 4! = 1.67 ; 40 % 4! = 16
## so its the 1st number (0, 3, 4, 5, 8)
## we need the 16th number that starts wtih 278391

## 16 / 3! = 2.67 ; 16 % 3! = 4
## so its the 2nd number (0, 4, 6)
## we need the 4th number that starts wtih 2783915.. (0, 4, 6)

## 1. 2783915046
## 2. 2783915064
## 3. 2783915406
## 4. 2783915460
 
def main():
  """docstring for main"""
            
if __name__ == "__main__":
    main()
