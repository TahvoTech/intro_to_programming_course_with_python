# COMP.CS.100 6.8 Isot alkukirjaimet paikoilleen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program capitalizes initial letters.

Example of the program in use:

>> capitalize_initial_letters("drIVING cAR")
'Driving Car'

>> capitalize_initial_letters("")
''

"""

def capitalize_initial_letters(text):
    """
    returns capitalized initial letters aka title text
    """
    capitalized_text = text.title()

    return capitalized_text


def main():

    capitalize_initial_letters("drIVING cAR")
    capitalize_initial_letters("")

if __name__ == "__main__":
    main()