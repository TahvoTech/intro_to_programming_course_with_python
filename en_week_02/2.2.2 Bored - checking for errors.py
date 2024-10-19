"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413
"""

def main():
    while True:
        bored = input("Answer Y or N: ")
        if bored.lower() == "y" or bored.lower() == "n" :
            print(f"You answered {bored}")
            break
        else:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()
'''

Task:

Bored? (checking for errors)

Learning Goals

Learning to implement a repeating structure where the user does not know the number of repetitions in advance (while).

The program you implemented in the previous section will not work properly when the user enters something other than "y", "Y", "n", or "N". Now, implement a whole new program, which only contains a repeating structure that asks the user's answer again if the answer is not "y", "Y", "n" or "N".

Examples of how the program operates:

Answer Y or N: q
Incorrect entry.
Answer Y or N: w
Incorrect entry.
Answer Y or N: n
You answered n

Answer Y or N: Y
You answered Y

Answer Y or N: N
You answered N

Programming tips:

    The solution is similar to the previous task's solution, but the condition of the repeating structure is more complicated. Use logical operators to combine the different parts of the condition.


'''