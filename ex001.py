"""Add all the natural numbers
    below one thousand that are
    multiples of 3 or 5."""

import datetime


def main():
    totalSum = 0
    for i in range(1000):
        if (i % 5 == 0) or (i % 3 == 0):
            totalSum += i

    print(totalSum)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print("Total Time: "
          + str((start_time - end_time).total_seconds())
          + " seconds.")
