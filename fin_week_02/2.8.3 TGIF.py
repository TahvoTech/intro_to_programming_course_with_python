# COMP.CS.100 2.8.3 TGIF
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Ohjelma, joka tulostaa vuoden 2014 kaikkien perjantaiden päivämäärät. Vuonna 2014 ensimmäinen perjantai oli 3.1.


"""

def main():
    months = 1
    days = 1
    friday = 5

    # Read answers while the value of the flag variable is True.
    while months <= 7:
        if months % 2 == 1:
            while days <= 31:
                if friday % 7 == 0:
                    print(f"{days}.{months}.")
                friday += 1
                days += 1
            months += 1
            days = 1
        elif months % 2 == 0:
            if months == 2:
                while days <= 28:
                    if friday % 7 == 0:
                        print(f"{days}.{months}.")
                    friday += 1
                    days += 1
            else:
                while days <= 30:
                    if friday % 7 == 0:
                        print(f"{days}.{months}.")
                    friday += 1
                    days += 1
            months += 1
            days = 1

    while months <= 12:
        if months % 2 == 1:
            while days <= 30:
                if friday % 7 == 0:
                    print(f"{days}.{months}.")
                friday += 1
                days += 1
            months += 1
            days = 1
        elif months % 2 == 0:
            while days <= 31:
                if friday % 7 == 0:
                    print(f"{days}.{months}.")
                friday += 1
                days += 1
            days = 1
            months += 1

if __name__ == "__main__":
    main()