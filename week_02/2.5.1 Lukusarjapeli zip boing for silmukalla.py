# COMP.CS.100 2.5.1 Lukusarjapeli zip boing for silmikalla
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
example of the program outcome:

How many numbers would you like to have? 10
1
2
zip
4
5
zip
boing
8
zip
10

"""

def main():

    end = int(input("How many numbers would you like to have? "))
    number = 1

    for _ in range(1, end + 1):
        if number % 3 == 0:
            if number % 7 == 0:
                print("zip boing")
            else:
                print("zip")
        elif number % 7 == 0:
            print("boing")
        else:
            print(number)
        number += 1


if __name__ == "__main__":
    main()
