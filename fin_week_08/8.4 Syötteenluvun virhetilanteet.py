# COMP.CS.100 8.4 Syötteenluvun virhetilanteet
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
This script prompts the user to enter the dimensions (width and height) and a mark character,
then prints a rectangular frame using the specified mark. The program ensures that the dimensions
entered are positive integers, demonstrating basic input validation and error handling in Python.

Functions:
- read_input: Prompts the user for a positive integer, validating the input.
- print_box: Prints a box of specified dimensions using a given mark.
- main: Drives the program by calling other functions to collect input and print the box.
"""

def read_input(prompt):
    """
    Repeatedly prompts the user for input until a positive integer is entered.

    Parameters:
    prompt (str): The prompt message to display to the user.

    Returns:
    int: A positive integer input by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except TypeError:
            # TypeError handling is unnecessary here because input() always returns a string.
            pass
        except ValueError:
            # Catching ValueError to handle non-integer inputs; silently retries.
            pass


def print_box(width, height, mark):
    """
    Prints a box made of a specified mark with the given width and height.

    Parameters:
    width (int): The width of the box.
    height (int): The height of the box.
    mark (str): The character used to draw the box.
    """
    print("")
    for i in range(height):
        print(mark * width)


def main():
    """
    Main function to drive the program. It prompts the user for the dimensions of the box
    and the character to use for drawing, then prints the box.
    """
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    # The following line should be updated as it incorrectly attempts to read a mark as an integer.
    # Instead, directly use input() to read the mark as a string.
    mark = input(
        "Enter a print mark: ")  # Corrected to use input() for string input.
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
