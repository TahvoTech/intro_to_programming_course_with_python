# COMP.CS.100 7.10 Tanssipelien pisteet
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
"""
program sums games and gives average of the amounts

"""

SONG_RESULT = {"Bubble dancer": 93.4, "The Game": 92.03, "Vertex": 75.3,
               "Lemmings on the Run": 86.2, "Da Roots": 96.02,
               "Charlene": 75.3, "Disconnected": 86.3, "Fly away": 87.32,
               "Hybrid": 63.9, "My favourite game": 89.45, "Oasis": 59.5,
               "Remember December": 96.3, "The beginning": 90.45,
               "Tribal Style": 87.45, "Why Me": 97.38, "Xuxa": 63.84,
               "Zodiac": 83.43, "Queen of Light": 75.12, "Mouth": 98.34,
               "Pandemonium": 79.31}

def calculate_average(dicti):
    """
    function sums values from dict param and divides it with the count of
    values in dict.

    :param: dict, dictionary with values
    """
    return sum(dicti.values()) / len(dicti)

def main():

    calculate_average(SONG_RESULT)

if __name__ == "__main__":
    main()