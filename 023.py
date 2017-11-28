"""
Find the sum of all the positive integers which
cannot be written as the sum of two abundant numbers.
"""

import math

def abundant(x):
  s = 1
  t = math.sqrt(x)
  for i in range(2, int(t)+1):
    if x % i == 0: s += i + x / i
  if t == int(t): s -= t
  return s

def main():
    """docstring for main"""
    totalSum = 0
    abn = set()
    for i in range(1, 28123):
        if abundant(i) > i:
            abn.add(i)
        if not any( (i-j in abn) for j in abn):
            totalSum += i

    print(totalSum)
        
        
            
if __name__ == "__main__":
    main()
