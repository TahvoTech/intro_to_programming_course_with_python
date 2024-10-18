# COMP.CS.100 6.4 Vokaalit ja konsonantit
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Program asks a word from the user and tells how many vowels there is.

Example of the program in use:

Enter a word: sassafrass
The word "sassafrass" contains 3 vowels and 7 consonants.
"""

def calculate_vowels(word):
    """
    funktio laskee ja palauttaa vokaalien ja konsonanttien määrän.
    """
    vowels = ["a","e","i","o","u","y"]
    vowel_count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_count += 1

    consonant_count = len(word) - vowel_count

    return vowel_count, consonant_count

def main():

    word = input("Enter a word: ")

    vowels, consonants = calculate_vowels(word)

    print(f"The word \"{word}\" contains {vowels} vowels and {consonants} "
          f"consonants.")

if __name__ == "__main__":
    main()