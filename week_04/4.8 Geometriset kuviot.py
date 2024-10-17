# COMP.CS.100 4.8 Geometriset kuviot
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Program asks to choose a geometric pattern or quit. If a pattern is chosen
the next requests are needed dimensions (rectangle's side, square's side,
circle's radius). After this prints circumference and
surface area with two decimals. program returns to the beginning if not quit.

if something else than s = square, r = rectangle, circle ja q = quit
then prints warning about incorrect entry.

minimum 7 own functions are added: examples:
def calculate_circumference
def calculate_rectangle_circumference
def calculate_circle_circumference
def calculate_square_circumference

def calculate_surface_area
def calculate_rectangle_surface_area
def calculate_circle_surface_area
def calculate_square_surface_area
def check_inputs

def change_capital_to_small_string_letter
def change_int_to_float
def change_to_two_decimals

def goodbye_text

Examples:

Enter the pattern's first letter or (q)uit: s
Enter the length of the square's side: 2.2
The circumference is 8.80
The surface area is 4.84

Enter the pattern's first letter or (q)uit: r
Enter the length of the rectangle's side 1: -4
Enter the length of the rectangle's side 1: 1.5
Enter the length of the rectangle's side 2: -3.5
Enter the length of the rectangle's side 2: 2.5
The circumference is 8.00
The surface area is 3.75

Enter the pattern's first letter or (q)uit: y
Incorrect entry, try again!

Enter the pattern's first letter or (q)uit: s
Enter the length of the square's side: 0
Enter the length of the square's side: -3
Enter the length of the square's side: 4
The circumference is 16.00
The surface area is 16.00

Enter the pattern's first letter or (q)uit: q
Goodbye!

"""

from math import pi
def calculate_rectangle_circumference(side_1, side_2):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    circumference = float(2 * side_1 + 2 * side_2)
    return print(f"The circumference is {circumference:.2f}")

def calculate_circle_circumference(radius):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    circumference = float(2*pi*radius)
    return print(f"The circumference is {circumference:.2f}")

def calculate_square_circumference(side):
    """ does what?

    :param : float, blaablaa.
    :return: text with float answer.
    """
    circumference = float(4 * side)
    return print(f"The circumference is {circumference:.2f}")

def calculate_rectangle_surface_area(side_1, side_2):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    surface_area = float(side_1*side_2)
    return print(f"The surface area is {surface_area:.2f}")

def calculate_circle_surface_area(radius):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    surface_area = float(pi*radius**2)
    return print(f"The surface area is {surface_area:.2f}")

def calculate_square_surface_area(side):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    surface_area = float(side*side)
    return print(f"The surface area is {surface_area:.2f}")

def goodbye_text(chosen_text):
    """ does what?

    :param : int, blaablaa.
    :return: int, blaablaa.
    """
    if chosen_text == "normal":
        return print("Goodbye!")

def main():

    pattern = "x"
    while pattern != "q":
        pattern = input("Enter the pattern's first letter or (q)uit: ")
        if pattern == "s":
            side = 0
            while side < 1:
                side = float(input("Enter the length of the square's side: "))
            calculate_square_circumference(side)
            calculate_square_surface_area(side)
            print("")
        elif pattern == "r":
            side_1 = 0
            side_2 = 0
            while side_1 < 1:
                side_1 = float(input("Enter the length of the rectangle's side 1: "))
            while side_2 < 1:
                side_2 = float(input("Enter the length of the rectangle's side 2: "))
            calculate_rectangle_circumference(side_1, side_2)
            calculate_rectangle_surface_area(side_1, side_2)
            print("")
        elif pattern == "c":
            radius = 0
            while radius <= 0:
                radius = float(input("Enter the circle's radius: "))
            calculate_circle_circumference(radius)
            calculate_circle_surface_area(radius)
            print("")
        elif pattern == "q":
            goodbye_text("normal")
        else:
            print("Incorrect entry, try again!")
            print("")


if __name__ == "__main__":
  main()