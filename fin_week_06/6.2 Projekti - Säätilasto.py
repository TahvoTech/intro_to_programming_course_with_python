# COMP.CS.100 6.2 Projekti - Säätilasto
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program shows which days were colder or warmer than average in the chosen
timeline.

examples:

Enter amount of days: 5
Enter day 1. temperature in Celsius: -3
Enter day 2. temperature in Celsius: -1
Enter day 3. temperature in Celsius: 0
Enter day 4. temperature in Celsius: 1
Enter day 5. temperature in Celsius: 3

Temperature mean: 0.0C
Temperature median: 0.0C

Over or at median were:
Day␣␣3.␣␣␣0.0C difference to mean:␣␣␣0.0C
Day␣␣4.␣␣␣1.0C difference to mean:␣␣␣1.0C
Day␣␣5.␣␣␣3.0C difference to mean:␣␣␣3.0C

Under median were:
Day␣␣1.␣␣-3.0C difference to mean:␣␣-3.0C
Day␣␣2.␣␣-1.0C difference to mean:␣␣-1.0C

AND

Enter amount of days: 7
Enter day 1. temperature in Celsius: -5
Enter day 2. temperature in Celsius: -4.2
Enter day 3. temperature in Celsius: 1.2
Enter day 4. temperature in Celsius: 5.1
Enter day 5. temperature in Celsius: -0.5
Enter day 6. temperature in Celsius: 2.4
Enter day 7. temperature in Celsius: 3

Temperature mean: 0.3C
Temperature median: 1.2C

Over or at median were:
Day␣␣3.␣␣␣1.2C difference to mean:␣␣␣0.9C
Day␣␣4.␣␣␣5.1C difference to mean:␣␣␣4.8C
Day␣␣6.␣␣␣2.4C difference to mean:␣␣␣2.1C
Day␣␣7.␣␣␣3.0C difference to mean:␣␣␣2.7C

Under median were:
Day␣␣1.␣␣-5.0C difference to mean:␣␣-5.3C
Day␣␣2.␣␣-4.2C difference to mean:␣␣-4.5C
Day␣␣5.␣␣-0.5C difference to mean:␣␣-0.8C

AND

Enter amount of days: 10
Enter day 1. temperature in Celsius: 1.5
Enter day 2. temperature in Celsius: 0.2
Enter day 3. temperature in Celsius: -5
Enter day 4. temperature in Celsius: -25
Enter day 5. temperature in Celsius: -3.1
Enter day 6. temperature in Celsius: -4.2
Enter day 7. temperature in Celsius: -27.7
Enter day 8. temperature in Celsius: -12.1
Enter day 9. temperature in Celsius: -5.1
Enter day 10. temperature in Celsius: 4.2

Temperature mean: -7.6C
Temperature median: -4.6C

Over or at median were:
Day␣␣1.␣␣␣1.5C difference to mean:␣␣␣9.1C
Day␣␣2.␣␣␣0.2C difference to mean:␣␣␣7.8C
Day␣␣5.␣␣-3.1C difference to mean:␣␣␣4.5C
Day␣␣6.␣␣-4.2C difference to mean:␣␣␣3.4C
Day␣10.␣␣␣4.2C difference to mean:␣␣11.8C

Under median were:
Day␣␣3.␣␣-5.0C difference to mean:␣␣␣2.6C
Day␣␣4.␣-25.0C difference to mean:␣-17.4C
Day␣␣7.␣-27.7C difference to mean:␣-20.1C
Day␣␣8.␣-12.1C difference to mean:␣␣-4.5C
Day␣␣9.␣␣-5.1C difference to mean:␣␣␣2.5C

"""

def calculate_mean(data):
    """
    Calculate the mean of a list of temperatures.

    :param: list, list of temperatures.
    :return: float, mean temperature.
    """
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_median(data):
    """
    calculates the median of a list of temperatures.

    :param: list, list of temperature values.
    :return: float, median temperature.
    """
    # make a new list where the members in the data is sorted from small to
    # large
    sorted_data = sorted(data)
    # the length that will be used to get the middle member(s)
    members_in_data = len(data)
    # with if code we use to check if the length of the data is even and then
    # we need to get the two middle members to get the median by divideing
    # their sum by 2.
    if members_in_data % 2 == 0:
        middle1 = sorted_data[members_in_data // 2 - 1]
        middle2 = sorted_data[members_in_data // 2]
        median = (middle1 + middle2) / 2
    # if length of data is odd, then we use else command to get the median
    # member.
    else:
        median = sorted_data[members_in_data // 2]
    # return median value to main function
    return median

def over_or_at_median(temp, median, mean):
    """
    prints days where temp is over or at median and gives values.

    :param: list, temperatures
    :param: float, median
    :param: float, median
    :return: none

    """
    print("Over or at median were:")
    # length that will be used in while loop as a range
    length = len(temp)
    index = 0

    while index < length:
        if temp[index] >= median:
            difference = temp[index] - mean
            print(f"Day {(index+1):2d}.{temp[index]:6.1f}C difference to mean:"
                  f"{difference:6.1f}C")
        index += 1

def under_median(temp, median, mean):
    """
    prints days where temp is under median and gives values.

    :param: list, temperatures
    :param: float, median
    :param: float, median
    :return: none

    """
    print("Under median were:")

    length = len(temp)
    index = 0

    while index < length:
        if temp[index] < median:
            difference = temp[index] - mean
            print(f"Day {(index+1):2d}.{temp[index]:6.1f}C difference to mean:"
                  f"{difference:6.1f}C")
        index += 1

def main():
    """
    Get temperature data from the user and calculate mean and median and use
    them in other functions.
    Print the results via functions along with temperatures above and below
    median.
    """
    num_of_days = int(input("Enter amount of days: "))
    temperatures = []

    # Ask temperatures from the user and add (append) them to the list
    for day_number in range(1, num_of_days + 1):
        temp = float(input(f"Enter day {day_number}. temperature in Celsius: "))
        temperatures.append(temp)

    mean = calculate_mean(temperatures)
    median = calculate_median(temperatures)

    # Print empty row to the beginnign, then the mean and median and one empty
    # row to the end.
    print("")
    print(f"Temperature mean: {mean:.1f}C")
    print(f"Temperature median: {median:.1f}C")
    print("")

    over_or_at_median(temperatures, median, mean)

    print("")

    under_median(temperatures, median, mean)

if __name__ == "__main__":
    main()