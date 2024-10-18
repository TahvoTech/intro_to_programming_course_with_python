# COMP.CS.100 9.5 TV-sarjan valitseminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

def main():

    eka = 0
    toka = 1

    while eka < 10:
        print(eka)
        eka = toka
        toka = toka + toka

if __name__ == "__main__":
    main()
