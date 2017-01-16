""" There exists exactly one
    Pythagorean triplet for which
    a + b + c = 1000.
    Find the product abc."""

def main():
    """docstring for main"""

    possA = []
    possB = []

    for i in range(1, 500):
        possA.append(i)
        possB.append(i)

    for a in possA:
        for b in possB:
            if a**2 + b**2 == (1000 - a - b)**2:
                c = 1000 - a - b
                print(a, b, c)

        
if __name__ == "__main__":
    main()
