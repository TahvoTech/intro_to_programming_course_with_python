# COMP.CS.100 3.6.3 Tulostetaan ruutu
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

elma tulostaa hienoja ruutuja tällä tavalla:

Enter the width of a frame: 6
Enter the height of a frame: 3
Enter a print mark: *

******
******
******

"""

def print_box(width, height, mark):
    """ prints a frame by using parameters for width, height and mark."""
    # tracker for while loop
    height_tracker = 1

    # while loop for making rows of parameter x
    while height_tracker <= height:
        print(mark*width)
        height_tracker += 1

def main():

    #request parameters from the client
    width = int(input("Enter the width of a frame: "))
    height = float(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    #print blank row
    print()
    # print the frame function
    print_box(width, height, mark)

if __name__ == "__main__":
    main()