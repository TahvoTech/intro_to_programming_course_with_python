# COMP.CS.100 6.6 Käännä nimet oikein päin
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program takes a name as a param and returns acronym.

Example of the program in use:

>> create_an_acronym("central intelligence agency")
'CIA'
"""

def create_an_acronym(text):
    """
    function creates an acronym from given words
    """
    list_of_words = text.split()
    list_of_upper_words = []
    for i in range(len(list_of_words)):
        list_of_upper_words.append(list_of_words[i].upper())
    acronym = ""
    for i in range(len(list_of_upper_words)):
        acronym += list_of_upper_words[i][0]

    return acronym

def main():

    create_an_acronym("central intelligence agency")


if __name__ == "__main__":
    main()
