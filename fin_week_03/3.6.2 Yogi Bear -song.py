# COMP.CS.100 3.6.2 Yogi Bear -song
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Program prints the Yogi Bear -song using functions.

"""

def repeat_name(name, repeats):
    """ repeat name part requested times """
    # to be able to use while looop, we need tracker start.
    tracker = 1

    # while loop here until repeats are done
    while tracker <= repeats:
        print(f"{name}, {name} Bear")
        tracker += 1
def verse(verse, name):
    """ this prints verse and uses repeat_name function as requested """
    # print verse
    print(f"{verse}")
    print(f"{name}, {name}")
    print(f"{verse}")
    # print part with repeats
    repeat_name(name, 3)
    print(f"{verse}")
    # print part with only one repeat
    repeat_name(name, 1)

def main():

    # first verse
    verse("I know someone you don't know", "Yogi")
    # print black row
    print("")
    # second verse
    verse("Yogi has a best friend too", "Boo Boo")
    # print black row
    print("")
    # third verse
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()