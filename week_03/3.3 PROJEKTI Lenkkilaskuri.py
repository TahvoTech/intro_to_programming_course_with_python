# COMP.CS.100 3.3 PROJEKTI: Lenkkilaskuri
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Running program:

Juostu sopiva määrä
Enter the number of days: 7
Enter day 1 running length: 3
Enter day 2 running length: 0
Enter day 3 running length: 0
Enter day 4 running length: 7
Enter day 5 running length: 8
Enter day 6 running length: 5.4
Enter day 7 running length: 7.1

You were persistent runner! With a mean of 4.36 km.
Juostu liian vähän
Enter the number of days: 9
Enter day 1 running length: 3.1
Enter day 2 running length: 2.2
Enter day 3 running length: 1
Enter day 4 running length: 2.8
Enter day 5 running length: 2.3
Enter day 6 running length: 0
Enter day 7 running length: 1.3
Enter day 8 running length: 1.5
Enter day 9 running length: 2.6

Your running mean of 1.87 km was too low!
Liian monta peräkkäistä päivää ilman juoksemista
Enter the number of days: 10
Enter day 1 running length: 3.3
Enter day 2 running length: 1.2
Enter day 3 running length: 4.2
Enter day 4 running length: 0
Enter day 5 running length: 0
Enter day 6 running length: 0

You had too many consecutive lazy days!

"""

def main():

    days = int(input("Enter the number of days: "))
    tracker = 1
    three_tracker = 0
    running_length_total = 0

    while tracker <= days:
        if three_tracker == 3:
            break
        running_length = float(input(f"Enter day {tracker} running length: "))
        if running_length != 0:
            three_tracker = 0
        running_length_total += running_length
        if running_length == 0:
            three_tracker += 1
        tracker += 1

    print("")

    mean_run = running_length_total / (tracker - 1)

    if three_tracker == 3:
        print("You had too many consecutive lazy days!")
    elif mean_run < 3:
        print(f"Your running mean of {mean_run:.2f} km was too low!")
    elif mean_run >= 3:
        print(f"You were persistent runner! With a mean of {mean_run:.2f} km.")


if __name__ == "__main__":
    main()