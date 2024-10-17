# COMP.CS.100 8.5
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413


def main():

    file = open("numbers.txt", mode="w")

    for i in range(1, 6):
        print(1.5 * i, file=file)

    file.close()

    filename = input("enter filename: ")

    try:
        file = open(f"{filename}.txt", mode="r", encoding="utf8")

    except OSError:
        print("some issue in opoeing the file")

    sum_total = 0
    try:
        for file_line in file:

            file_line = file_line.rstrip()
            print(file_line)
            try:
                number = float(file_line)

            except ValueError:
                print(file_line, "not a float")

            sum_total += number
    except OSError:
        print("issue with file")

    print(sum_total)

if __name__ == "__main__":
    main()