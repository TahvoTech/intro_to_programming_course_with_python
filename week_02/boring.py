"""
COMP.CS.100 Programming 1, Fall 2023, Lecture 2.
Author: Jorma Laurikkala
Student number: ---------

Reads and repeats 10 words. A counter variable controls the loop.
Modified code from the Plussa material.
"""

def main():
    # A counter variable is initialized to a common starting
    # value when counting up.
    nwords_read = 0

    # Read words while less than has been entered.
    while nwords_read < 10:
        # Read and print a word.
        word = input("Please, enter a word: ")
        print("You said:", word)

        # Increase the counter.
        nwords_read = nwords_read + 1
        print(nwords_read)

if __name__ == "__main__":
    main()
