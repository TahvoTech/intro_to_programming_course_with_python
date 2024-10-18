# COMP.CS.100 5.6.1 Arvosanojen korvaus
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Program changes grades 1-5 to value 6.

"""

# TODO: add the definition for convert_grades here

def convert_grades(elements):
    """
    function converts grades 1-5 to 6.

    :param: int, grades.
    :return: no return.
    """

    lenght = len(elements)

    for i in range(lenght):
        if elements[i] > 0:
            elements[i] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

if __name__ == "__main__":
    main()