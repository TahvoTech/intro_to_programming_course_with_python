# COMP.CS.100 8.9 Numeroitujen rivien kirjoittaminen tiedostoon
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
eaegeag
ag
ag
aeg
ag
ge
"""

"""
def read_message(file_name):

    try:
        read_file = open(file_name, mode="r")

        for text_line in read_file:
            text_line = text_line.strip()
            print(text_line)
    except OSError:
        print("not possilbe")

    read_file.close()


"""

def main():

    file_name = input("Enter the name of the file: ")

    try:

        save_file = open(file_name, mode="w")



        index = 1

        print("Enter rows of text. Quit by entering an empty row.")
        while True:
            text_line = input()
            if text_line == "":
                break
            print(f"{index} {text_line}", file=save_file)
            index += 1

        save_file.close()
        print(f"File {file_name} has been written.")

    except OSError:
        print(f"Writing the file {file_name} was not successful.")



#    read_message(file_name)





if __name__ == "__main__":
    main()
