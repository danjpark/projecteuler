"""
    http://projecteuler.net/problem=22
"""

import string
import csv

def main():
    """docstring for main"""

    retValue = 0
    tempValue = 0

    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 1
    values["\""] = 0
    print(values)
   
    reader = open(".//names.txt", "rt")

    for line in reader: split_reader = line.split(",")
    split_reader.sort()

    for item in split_reader:
        for alaphabet in item: tempValue += values[alaphabet]
        retValue += tempValue * (split_reader.index(item) + 1)
        tempValue = 0

    print(retValue)
    reader.close()
            
if __name__ == "__main__":
    main()
