# COMP.CS.100 4.10.1 Kolmion kulmien laskeminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program calculates angle for the third angle after the first two are given.

Examples in console:

calculate_angle(50, 60)
70
calculate_angle(30)
60

"""

def calculate_angle(angle_1, angle_2 = 90):
    """

    :param: angle_1, int, angle of the first angle
    :param: angle_2, int, angle of the first angle

    :return: none
    """
    angle_3 = 180 - angle_1 - angle_2
    return angle_3

def main():
    calculate_angle()

if __name__ == "__main__":
  main()