# COMP.CS.100 2.8.2 vuoden paivamaarat
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Tee ohjelma, joka tulostaa sellaisen vuoden päivämäärät, joka ei ole karkausvuosi:

1.1.
2.1.
3.1.
4.1.
5.1.
...
31.1.
1.2.
2.2.
3.2.
...
28.2.
1.3.
...

"""

def main():
    months = 1
    days = 1

    # Read answers while the value of the flag variable is True.
    while months <= 7:
        if months%2 == 1:
            while days <= 31:
                print(f"{days}.{months}.")
                days += 1
            months += 1
            days = 1
        elif months % 2 == 0:
            if months == 2:
                while days <= 28:
                    print(f"{days}.{months}.")
                    days += 1
            else:
                while days <= 30:
                    print(f"{days}.{months}.")
                    days += 1
            months += 1
            days = 1
    while months <= 12:
        if months%2 == 1:
            while days <= 30:
                print(f"{days}.{months}.")
                days += 1
            months += 1
            days = 1
        elif months % 2 == 0:
            if months == 2:
                while days <= 28:
                    print(f"{days}.{months}.")
                    days += 1
            else:
                while days <= 31:
                    print(f"{days}.{months}.")
                    days += 1
            months += 1
            days = 1
if __name__ == "__main__":
    main()