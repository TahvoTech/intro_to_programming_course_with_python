# COMP.CS.100
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413


def main():

    feeling = int(input("How do you feel? (1-10) "))

    if feeling > 0 and feeling < 11:
        if feeling == 1:
            print("A suitable smiley would be :'(")
        elif feeling == 10:
            print("A suitable smiley would be :-D")
        elif feeling > 7:
            print("A suitable smiley would be :-)")
        elif feeling < 4:
            print("A suitable smiley would be :-(")  
        else:
            print("A suitable smiley would be :-|")
    else:
        print("Bad input!")

"""
    if feeling > 10 or feeling < 1:
        print("Bad input!")

    elif feeling > 7:
        print("A suitable smiley would be :-)")

    else:
        print("A suitable smiley would be :-|")
"""

if __name__ == "__main__":
    main()








'''
Learning Goals

Review if, elif, and else.

a)

Create a program that asks the user how they feel on scale 1-10 and then proposes a suitable emoticon to describe the mood. First implement a relatively expressionless version that prints :-) for feelings over 7 and otherwise prints the basic face :-|.

Examples of how the program works:

How do you feel? (1-10) 6
A suitable smiley would be :-|

and

How do you feel? (1-10) 9
A suitable smiley would be :-)

You can return this task for the first time at this phase. An automatic evaluation offers a partial score for each subsection. You receive a full score when every subsection operates correctly.

Programming tips:

    You need a variable for saving the value entered by the user. This variable is used in the condition of the if structure. Think about this variable’s data type. (Is it a floating-point number or an integer?)

    Use an if-else structure, as the assignment has defined a Condition for when to print :-), and :-| is printed in all the other cases.

    When you test your program, pay attention to the values on the threshold. These include the largest value for printing :-| and the smallest value for printing :-) Which values are these?

b)

Now make the previously mentioned program verify the numeric values - if something other than a numeric value between 1 and 10 is entered, the program should print Bad input!

Otherwise, the program should operate like in section a), but an example of an error of this sort would be:

How do you feel? (1-10) 42
Bad input!

Programming tips:

    The program will include two inner if structures. The first (outer) if structure checks whether the entered number is incorrect and either prints an error message or recommends an emoticon. The second (inner)if structure, which recommends an emoticon, is the one implemented in section a).

    If you are having trouble picturing the situation, draw yourself a number line and mark which part of the number line is connected to which part of the if structure.

    Think about the values that should be used to test the program. How many more values to be tested are there than in section a)?

c)

You should be able to express negative emotions when necessary, so let’s add the program a sad emoticon :-(, which is recommended for feelings that are less than 4.

Examples:

How do you feel? (1-10) 2
A suitable smiley would be :-(

Programming tips:

    Familiarize yourself with the elif structure. A feeling expressed using one value is very one-dimensional: if the user is happy, the program no longer needs to check if they’re sad. Thus, this change can be done the most logically by adding an elif part to an if-else structure.

    You can also consider how to implement the program not using any else or elif parts.

    Think again about the values used to test the program. How many more tested values are there now than in sections a) and b)?

d)

Let’s add more expressiveness to the program. The extremes of the emotion scale, the values 1 and 10, use the stronger faces :'( and :-D.

Examples of program running:

How do you feel? (1-10) 1
A suitable smiley would be :'(

and

How do you feel? (1-10) 10
A suitable smiley would be :-D

Programming tips:

    There can be several elif parts one after another, so this only needs a few small changes to the previous part.

    Use a number line for planning the conditions for if and elif.

'''