# COMP.CS.100 2.2.1 Onko tylsää?
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Reads answers n or y and stops when answer is n.

"""

def main():
    read_answers = True

    # Read answers while the value of the flag variable is True.
    while read_answers:
        answer = input("Bored? (y/n) ")
        # Evaluate a new value for the flag variable.
        read_answers = answer != "y"
        if answer != "n"
            print("wrong answer")

    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()