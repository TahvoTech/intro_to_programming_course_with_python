# COMP.CS.100 2.8.1 Onko tylsää parannettu versio
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""



Reads all answers and stops when answer is n,N,y or Y.

ohjelma kysyy, onko tylsää, kunnes on, ja lisäksi vaaditaan,
että vastauksena pitää antaa jokin kirjaimista "y", "Y", "n" tai "N",
eli vastausta kysytään uudelleen, kunnes on saatu jokin kelvollinen syöte.


Esimerkkejä ohjelman toiminnasta:

Bored? (y/n) o
Incorrect entry.
Bored? (y/n) z
Incorrect entry.
Bored? (y/n) m
Incorrect entry.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) f
Incorrect entry.
Bored? (y/n) j
Incorrect entry.
Bored? (y/n) y
Well, let's stop this, then.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.


"""

def main():
    read_answers = True

    # Read answers while the value of the flag variable is True.
    while read_answers:
        answer = input("Bored? (y/n) ")
        # Evaluate a new value for the flag variable.
        if answer == "n" or answer == "N":
            read_answers = True
        elif answer == "y" or answer == "Y":
            read_answers = False
            print("Well, let's stop this, then.")
        else:
            print("Incorrect entry.")


if __name__ == "__main__":
    main()