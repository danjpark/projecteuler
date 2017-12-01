"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math




def main():
  """docstring for main"""
  last_number = 1
  last_last_number = 1
  temp = 0
  counter = 2

  for i in range(100000):
    temp = last_number + last_last_number
    last_last_number = last_number
    last_number = temp
    counter += 1
    
    if len(str(last_number)) == 1000:
      print(counter)
      return

            
if __name__ == "__main__":
    main()
