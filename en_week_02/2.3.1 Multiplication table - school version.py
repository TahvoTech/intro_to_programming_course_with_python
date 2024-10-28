"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413
"""

def main():
    
    number = int(input("Choose a number: "))
    reps = 10
    counter = 1

    while counter <= reps:
        print(f"{counter} * {number} = {counter * number}")
        counter += 1


if __name__ == "__main__":
    main()


'''

Task:

Multiplication table, school version

Learning Goals

Learning to implement a repetition using a while structure so that the number of times for repetition is known in advance. You can also use a for structure, but the instructions are for a while structure.

Create a program that prints a multiplication table for an entered number just like in school, using steps of one to ten.

Example:

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
10 * 6 = 60

Programming tips:

    When implementing this program, you will have a loop that contains a loop variable. Think about which part of the printing calculation operation uses the loop variable.


'''