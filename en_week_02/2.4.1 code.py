"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413

This module contains a number series game called "Zip Boing".
The game involves players taking turns to count up from 1, but replacing certain numbers with the words "Zip" or "Boing" based on specific rules.
Rules:
- Replace any number divisible by 3 with "zip".
- Replace any number divisible by 7 with "boing".
- Replace any number divisible by both 3 and 7 with "zip boing".
The game continues until a predetermined number is reached.
Functions:
- (List any functions here if applicable)
"""

def main():

    # Get the user input
    try:
        max_number = int(input("How many numbers would you like to have? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Loop through the numbers

    for i in range(1, max_number + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
        elif i % 3 == 0:
            print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)

if __name__ == "__main__":
    main()


