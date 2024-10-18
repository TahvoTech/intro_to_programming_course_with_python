# COMP.CS.100 5.5.3 Rubikin kuutio -kilpailut
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Rubiks cube

example:

Enter the time for performance 1: 5.80
Enter the time for performance 2: 5.40
Enter the time for performance 3: 5.17
Enter the time for performance 4: 5.19
Enter the time for performance 5: 5.22
The official competition score is 5.27 seconds.


"""

def times_for_performance():
    """funktio are_all_members_same, joka ottaa parametrinaan listan ja
    palauttaa tiedon siitä ovatko kaikki listan sisältämät alkiot samoja

    :Param: list
    :Return: bool, returns true / false if all the members in the list are same
    or not.
    """
    times = []
    for i in range(1, 6):
        times.append(float(input(f"Enter the time for performance {i}: ")))

    times.remove(min(sorted(times)))
    times.remove(max(sorted(times)))
    print(f"The official competition score is {(sum(times) / len(times)):.2f} "
          f"seconds.")

def main():

    times_for_performance()

if __name__ == "__main__":
    main()