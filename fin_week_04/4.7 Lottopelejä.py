# COMP.CS.100 4.7 Lottopelejä
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

program asks to values:

lottery balls total and drawn amoutn of balls. and gives a probability of
winnign with one ticket.

also the following wrning prints:
"The number of balls must be a positive number." "At most the total number of
balls can be drawn."

Examples:

Enter the total number of lottery balls: 39
Enter the number of the drawn balls: 7
The probability of guessing all 7 balls correctly is 1/15380937

Enter the total number of lottery balls: -3
Enter the number of the drawn balls: 4
The number of balls must be a positive number.

Enter the total number of lottery balls: 30
Enter the number of the drawn balls: 31
At most the total number of balls can be drawn.

"""


def calculate_factorial(x):
    """ calculates factorial

    :param : int, give number where to calculate factorial for.
    :return: int, factorial number
    """

    factorial_number = 1
    luku = 1
    while luku <= x:
        factorial_number = factorial_number * luku
        luku += 1
    return factorial_number

def lottery_probability(n, p):
    """ Function calculates the probability.

    :param : total_balls, total number of lottery balls
    :param : drawn_balls, number of drawn lottery balls
    :return: int, probability to win in lottery with just one ticket
    """

    probability = calculate_factorial(n) / (calculate_factorial(n-p)
                                            * calculate_factorial(p))

    return int(probability)

def main():
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    if total_balls < 0:
        print("The number of balls must be a positive number.")

    elif drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")

    else:
        result = lottery_probability(total_balls, drawn_balls)
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{result}")

if __name__ == "__main__":
  main()