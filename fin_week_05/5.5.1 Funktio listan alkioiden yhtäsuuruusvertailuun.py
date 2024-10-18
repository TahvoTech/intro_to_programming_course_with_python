# COMP.CS.100 5.5.1 Funktio listan alkioiden yhtäsuuruusvertailuun
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

def are_all_members_same(members):
    """funktio are_all_members_same, joka ottaa parametrinaan listan ja
    palauttaa tiedon siitä ovatko kaikki listan sisältämät alkiot samoja

    :Param: list
    :Return: bool, returns true / false if all the members in the list are same
    or not.
    """
    compare_list = []

    for i in range(len(members)):
        compare_list.append(members[0])
    if compare_list == members:
        return True
    else:
        return False

    new_list = []
    for i in range(len(members)):
        if compare_list[i] > members[i]:
            new_list.append(members[0])
    print(new_list)
    print(compare_list)
    print(members)

def main():
    are_all_members_same([42, 42, 42, 43, 42])
    are_all_members_same([42, 42, 42, 42])

if __name__ == "__main__":
    main()