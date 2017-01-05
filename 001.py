"""Add all the natural numbers
    below one thousand that are
    multiples of 3 or 5."""


def main():
    totalSum = 0
    for i in range(1000):
        if (i % 5 == 0) or (i % 3 == 0):
            totalSum += i

    print(totalSum)


if __name__ == "__main__":
    main()
