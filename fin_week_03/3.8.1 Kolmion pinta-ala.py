# COMP.CS.100 3.8.1 Trangle's Area when the Sides Are Known
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Function prints the trangle's area when the Sides Are Known

Example:
Enter the length of the first side: 2.5
Enter the length of the second side: 3
Enter the length of the third side: 4.5
The triangle's area is 3.5

"""

from math import sqrt

def area(first_side, second_side, third_side):
    """ calculate and return the area of a triangle whose three sides are given as parameters
    <<first_side>>, <<second_side>> and <<third_side>>. The function uses the standard formula
    to calculate the area of a triangle.

    :param first_side: float, the first side of a triangle
    :param second_side: float, the second side of a triangle
    :param third_side: float, the third side of a triangle
    :return: float & only 1 decimal, the area of the triangle
    """
    half = (first_side + second_side + third_side)/2
    result = sqrt(half * (half - first_side) * (half - second_side) * (half - third_side))

    return result

def main():
    line_1 = float(input("Enter the length of the first side: "))
    line_2 = float(input("Enter the length of the second side: "))
    line_3 = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {(area(line_1, line_2, line_3)):.1f}")

if __name__ == "__main__":
    main()
