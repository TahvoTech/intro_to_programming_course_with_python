# COMP.CS.100 5.7 Bussiaikataulu
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Program changes grades 1-5 to value 6.

"""

# TODO: add the definition for convert_grades here
BUS_TIMETABLE = [630, 1015, 1415, 1620, 1720, 2000]


def next_departures(time_now):
    """
    funcgtion shows next three departures from the time now.
    """
    length = len(BUS_TIMETABLE)

    next_three_departures = 3
    for i in range(length):
        if BUS_TIMETABLE[i] >= time_now and next_three_departures > 0:
            print(f"{BUS_TIMETABLE[i]}")
            next_three_departures -= 1
    if next_three_departures == 2:
        print(f"{BUS_TIMETABLE[0]}")
        print(f"{BUS_TIMETABLE[1]}")

    elif next_three_departures == 1:
        print(f"{BUS_TIMETABLE[0]}")

    elif next_three_departures == 3:
        print(f"{BUS_TIMETABLE[0]}")
        print(f"{BUS_TIMETABLE[1]}")
        print(f"{BUS_TIMETABLE[2]}")

def main():

    time_now = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    next_departures(time_now)


if __name__ == "__main__":
    main()