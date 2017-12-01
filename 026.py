"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators
2 to 10 are given:


1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d
contains the longest recurring cycle in its
decimal fraction part.
"""

import math

def how_many_repeats(x):
  """
    takes in int and returns an int
    how many numbers in a reoccuring cycle given 1/x
    returns 0 if not repeating
  """
  int(x) # should be zero
  for i in range(1, 10):
    if ((1 / x) * 10**i) % 10 == 0:
      return 0
    print(type((1/x) * (10**i) - (1/x)))
      
  return 1
    

def main():
  """docstring for main"""
  mostRepeating = 1
  number_mostRepeat = 1
  
  for i in range(1,10):
    temp = how_many_repeats(i)
    print(i, temp)
##    if temp >= number_mostRepeat:
##      mostRepeating = i
##      number_mostRepeat = temp

##  print(mostRepeating, number_mostRepeat)    
            
if __name__ == "__main__":
    main()
