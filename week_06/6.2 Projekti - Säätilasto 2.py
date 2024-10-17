# COMP.CS.100 6.2 Projekti - Säätilasto
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

def calculate_mean(data):
    """
    Calculate the mean of a list of temperatures.

    :param data: list of float, list of temperature values.
    :return: float, the mean temperature.
    """
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_median(data):
    """
    Calculate the median of a list of temperatures.

    :param: list of float, list of temperature values.
    :return: float, the median temperature.
    """
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_data[n // 2]
    return median

def main():
    """
    Get temperature data from the user and calculate mean and median.
    Print the results along with temperatures above and below median.
    """
    num_of_days = int(input("Enter amount of days: "))
    temperatures = []

    # Enter temperatures from the user and append them to the list
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

    print("Over or at median were:")
    for i, temp in enumerate(temperatures, start=1):
        if temp >= median:
            difference = temp - mean
            # Print temperatures above or at the median
            print(f"Day {i:<3d}. {temp:.1f}C difference to mean:"
                  f" {difference:.1f}C")

    print("Under median were:")
    for i, temp in enumerate(temperatures, start=1):
        if temp < median:
            difference = temp - mean
            # Print temperatures below the median
            print(f"Day {i:<3d}. {temp:.1f}C difference to mean:"
                  f" {difference:.1f}C")

if __name__ == "__main__":
    main()