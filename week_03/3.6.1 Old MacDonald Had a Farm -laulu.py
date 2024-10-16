# COMP.CS.100 3.6.1 Old MacDonald Had a Farm -song
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Old MacDonald Had a Farm -song using print_verse function to
insert animal and sound parameters to the verse.

"""

def print_verse(animal, sound):
    """Old MacDonald Had a Farm song verses."""
    print(f"Old MACDONALD had a farm")
    print("E-I-E-I-O")
    # print row with parameter(s)
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    # print row with parameter(s)
    print(f"With a {sound} {sound} here")
    # print row with parameter(s)
    print(f"And a {sound} {sound} there")
    # print row with parameter(s)
    print(f"Here a {sound}, there a {sound}")
    # print row with parameter(s)
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():

    # print verse with animal and sound
    print_verse("cow", "moo")
    # print black row
    print("")
    # print verse with animal and sound
    print_verse("pig", "oink")
    # print black row
    print("")
    # print verse with animal and sound
    print_verse("duck", "quack")
    # print black row
    print("")
    # print verse with animal and sound
    print_verse("horse", "neigh")
    # print black row
    print("")
    # print verse with animal and sound
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()