# COMP.CS.100 2.4.1 Lukusarjapeli zip boing
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
example of the program outcome:

How many numbers would you like to have? 10
1
2
zip
4
5
zip
boing
8
zip
10

"""

def main():

    # First we set the repetition counter for the while loop
    repetition_counter = 1
    chosen_number = int(input("How many numbers would you like to have? "))

    # set the while loop where every third repetition will print zip and seventh will print boing
    # and other repetitions prints the current repetition number.
    while repetition_counter <= chosen_number:
        if repetition_counter % 3 == 0:
            if repetition_counter % 7 == 0:
                print("zip boing")
            else:
                print("zip")
        elif repetition_counter % 7 == 0:
            print("boing")
        else:
            print(repetition_counter)
        repetition_counter += 1

if __name__ == "__main__":
    main()
