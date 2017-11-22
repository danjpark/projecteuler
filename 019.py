""" How many Sundays fell on the first
    of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime
from datetime import date


def main():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # weekday 0 is monday
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1

    print(count)
        
    
            
if __name__ == "__main__":
    main()
