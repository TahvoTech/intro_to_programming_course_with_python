# COMP.CS.100 5.5.2 Funktio listan suuruusjärjestyksen tarkasteluun
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Tee funktio are_all_members_same, joka ottaa parametrinaan listan ja palauttaa tiedon siitä ovatko kaikki listan sisältämät alkiot samoja.

Esimerkkejä funktion toiminnasta, kun sitä testataan Python-konsolissa:

>> are_all_members_same([42, 42, 42, 43, 42])
False
>> are_all_members_same([42, 42, 42, 42])
True
"""

def is_the_list_in_order(members):
    """funktio are_all_members_same, joka ottaa parametrinaan listan ja
    palauttaa tiedon siitä ovatko kaikki listan sisältämät alkiot samoja

    :Param: list
    :Return: bool, returns true / false if all the members in the list are same
    or not.
    """

    if members == sorted(members):
        return True
    else:
        return False

def main():
    is_the_list_in_order([37, 42, 43])
    is_the_list_in_order([42, 37, 43])

if __name__ == "__main__":
    main()