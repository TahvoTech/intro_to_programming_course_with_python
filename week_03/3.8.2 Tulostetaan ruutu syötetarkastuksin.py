# COMP.CS.100 3.8.2 Tulostetaan ruutu syötetarkastuksin
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

program prints fine frames and only accepts positive numbers.

Example:

Enter the width of a frame: -1
Enter the width of a frame: 0
Enter the width of a frame: -4
Enter the width of a frame: 4
Enter the height of a frame: -1
Enter the height of a frame: 0
Enter the height of a frame: 2
Enter a print mark: #

####
####
"""

def read_input(number):
    """asks for an input.
    :param number: first saved as a string and used to ask for
    positive input. inputs are saved as integers.
    :return: integer, the number for either width or heights of the frame.

    """
    input_text = number
    number = int(input(number))
    while number <= 0:
        number = int(input(input_text))
    return number

def print_box(width, height, mark):
    """ prints a frame by using parameters for width, height and mark."""
    # tracker for while loop
    height_tracker = 1

    # while loop for making rows of parameter x
    while height_tracker <= height:
        print(mark*width)
        height_tracker += 1

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()