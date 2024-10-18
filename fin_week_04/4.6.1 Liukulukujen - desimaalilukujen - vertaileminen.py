# COMP.CS.100 4.6.1 Liukulukujen - desimaalilukujen - vertaileminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Program compares two float numbers and returns true or false.

Examples:

compare_floats(0.00000000000000000001, 0.0000000000000000002)
True

compare_floats(0.0002, 0.0000002, EPSILON)
False

"""

EPSILON = 0.000000001


def compare_floats(first_float, second_float, EPSILON):
    """function compares two floats numbers.

    :param : float, first float number.
    :return: float, second float number.
    """
    if abs(first_float-second_float) < EPSILON:
        return True
    else:
        return False

def main():
    first_float = float(input())
    second_float = float(input())
    compare_floats(first_float, second_float, EPSILON)

if __name__ == "__main__":
  main()