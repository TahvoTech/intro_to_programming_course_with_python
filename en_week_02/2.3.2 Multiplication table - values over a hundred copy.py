"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413
"""

def main():

    number = int(input("Choose a number: "))
    limit = 100
    reps = limit // number + 1
    counter = 1

    while counter <= reps:
        print(f"{counter} * {number} = {counter * number}")
        counter += 1 

# OR

'''
    number = int(input("Choose a number: "))
    sum = 0
    counter = 1
    limit = 100

    while sum < limit:
        print(f"{counter} * {number} = {counter * number}")
        sum = counter * number
        counter += 1

'''



if __name__ == "__main__":
    main()



'''

Task:

Multiplication table, values over a hundred

Learning Goals

Creating a repetition structure where the number of repetitions is not known (calculated) in advance. Comparing the repetition structure to the repetition structure implemented in the previous part.

Create a program that prints a multiplication table for a given number until it reaches a result that is more than hundred.

Example:

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
17 * 6 = 102

Programming tips:

    One possible way is calculating the number of needed multiplications at the start of the program. Apart from the calculation, this does not differ too much from the implementation of the program in the previous part and thus teaches nothing new.

    Another possibility, more interesting for learning purposes, is to re-think the type of the loop structure (while or for) and the condition of the loop structure. What needs to be checked on every repetition?


'''