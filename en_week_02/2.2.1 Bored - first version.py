"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413
"""

def main():
    while True:
        bored = input("Bored? (y/n) ")
        if bored.lower() == "y":
            print("Well, let's stop this, then.")
            break  # Exit the loop when bored is "y"

if __name__ == "__main__":
    main()
'''

Task:

Bored? (first version)

Note

Learning to implement a repeating structure where the number of times a repetition happens is not known in advance (while).

Create a program that asks the user if they're bored, until they are. S Some examples of how the program works:

Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.

and:

Bored? (y/n) y
Well, let's stop this, then.

In this initial version, you may assume the user always answers either "y" or "n". There's no need to worry about incorrect entries. In practice, this means that you're only checking if the user's answer to question is "n", as this is the answer that continues the repetition.

Programming tips:

    Remember that in Python program code, a string including a letter X is marked "X". Instead, mere X without quotation marks refers to a variable named X. If you thus wish to create a variable called answer with the string "X" as a value, enter answer = "X" in Python.

    Your program needs a variable for saving the answer entered by the user. Which value should you use for formatting the variable? (In other words, which original value should you set to the variable?)

    Create a while structure in the program and use its condition to review this variable's value, ie. make the repetition (query) continue if the user answers that they are not bored. Create the while structure so, that the code in the structure is run if the condition is true.

    After the repetition ends, print a final message. In the program code file, this print command should be located after the repetition structure. Use indentation to show the repeated statements (indented inside the repetition structure) and the place where the program implementation continues when the repetition ends (indented on the same level as the word while).

    The program can be implemented so that the same input command is in two different sections of the program code, but also so that the input is only performed once. Can you implement the program so that only one input command is needed?

Which program rows of your program code are executed if you enter the example inputs given in this task as inputs? List the numbers of the performed rows in order. (You don't need to return this task, but should still understand its point.)


'''