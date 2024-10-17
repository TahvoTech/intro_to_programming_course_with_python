"""
Program reads and sums the real numbers
contained in a user specified file.
There must be exactly one number per line.
"""

def main():
    filename = input("Enter the filename containing the numbers: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print(f"Error: opening the file '{filename}' failed!")
        return

    sum_total = 0

    for file_line in file:


        file_line = file_line.rstrip()


        # Tiedostosta luettu tekstirivi on muutettava reaaliluvuksi,
        # jotta sillä voidaan suorittaa yhteenlasku rivillä 37.
        # Se tapahtuu periaatteessa suoraviivaisesti float-funktiolla.
        # On kuitenkin mahdollista, että luettu rivi ei olekaan
        # muodoltaan reaaliluku, jolloin float-funktio tuottaa
        # poikkeuksen ValueError.

        if file_line == "":
            continue

        line_parts = file_line.split()

        print(line_parts)

        for number_string in line_parts:

            try:
                number = float(number_string)

            except ValueError:
                print(f"Error: the value '{number_string}' is not a float!")
                return

            sum_total += number

    file.close()

    print(f"The sum of all the numbers in {filename} is {sum_total}.")
    print("")
    print((line_parts))


if __name__ == "__main__":
    main()
