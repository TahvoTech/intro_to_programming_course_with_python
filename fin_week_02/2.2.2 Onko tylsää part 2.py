# COMP.CS.100 2.2.1 Onko tylsää?
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Reads all answers and stops when answer is n,N,y or Y.

"""

def main():
    read_answers = True

    # Read answers while the value of the flag variable is True.
    while read_answers:
        answer = input("Answer Y or N: ")
        # Evaluate a new value for the flag variable.
        read_answers = answer != "y" and answer != "Y" and answer != "n" and answer != "N"
        #        OR read_answers = answer not in {"y", "y", "N", "n"}
        if read_answers:
            print("Incorrect entry.")
#        if answer == "n" and "N":
#            print("You answered", answer)

    print("You answered", answer)

if __name__ == "__main__":
    main()