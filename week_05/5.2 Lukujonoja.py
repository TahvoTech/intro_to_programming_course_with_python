# COMP.CS.100 5.2 Lukujonoja
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program calculates angle for the third angle after the first two are given.

Example run:

0
2
4
6
⋮
98
100
100
98
⋮
4
2
0

"""

def main():
    number = 0
    for i in range(0, 202):
        if number <= 100 and number % 2 == 0:
            print(f"{number}")
        elif number >= 100 and number % 2 != 0:
            print(f"{201 - number}")
        number += 1

    for i in range(0, 101, 2):
        print(i)

    for i in range(100, -1, -2):
        print(i)

if __name__ == "__main__":
  main()