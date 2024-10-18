# COMP.CS.100 4.11.1 Paranneltu ruudun tulostus
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program calculates angle for the third angle after the first two are given.

Examples:

#####
#   #
#   #
#####

***
* *
* *
* *
* *
* *
* *
***

OOOOO
OoooO
OoooO
OOOOO

OOOOOO
O....O
O....O
OOOOOO

"""

def print_box(width, height, border_mark = "#", inner_mark = " "):
    """
    function prints boxes according to parameters and have some default
    values as well.

    :param: int, width
    :param: int, height
    :param: str, border_mark
    :param: str, inner_mark
    :return:
    """
    print(width * border_mark)
    for i in range(height - 2):
        print(border_mark + inner_mark * (width - 2) + border_mark)
    print(width * border_mark)
    print("")

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
  main()