# COMP.CS.100 8.8
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

"""

def main():

    write_file = open("save_file.txt", mode="w")

    print("Shut up and take my money!", file=write_file)


if __name__ == "__main__":
    main()