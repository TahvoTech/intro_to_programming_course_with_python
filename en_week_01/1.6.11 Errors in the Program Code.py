"""
COMP.CS.100 Programming 1
developer: Jarmo Tahvanainen
email: jarmo.tahvanainen@gmail.com
student id: 151737413
"""
"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""

def main():
    age = int(input("Please, enter your age: "))

    if age >= 25:
        ticket_price = 2.04
    elif age >= 17:
        ticket_price = 1.47
    elif age >= 7:
        ticket_price = 1.02
    else:
        ticket_price = 0.00

    print(f"Your ride will cost: {ticket_price}")


if __name__ == "__main__":
    main()
'''
Errors in the Program Code

Learning Goals

To learn the basic meaning of the error messages Python prints when there is an error in a program code.

When writing computer programs there are basically three kind of errors one can face: 1

Syntax errors

    When talking about human languages syntax errors are usually called grammatical errors. In computer programming syntax error means that the erroneous program contains something that is against the grammar rules of the programming language.

    For example the following program line results a syntax error in Python:

    print("Hello)

    This is because the grammar rules of Python require every string literal which starts with a double quote must also end with one. In the example someone had forgotten to add the closing double quote.

    If we try to run this program here is what happens:

    File "<test.py>", line 1
    print("Hello)
                ^
    SyntaxError: EOL while scanning string literal

    Whenever Python interpreter meets a syntax error in the program it prints a line beginning with the word SyntaxError followed by an explanation for the error and preceeded by description of the error location. Python even let's us know the line number in the source file where it thinks the error is located. Unfortunaltely sometimes things might get more confusing, but in general the error messages given by Python are very clear and informative compared to some other programming languages.

    After the SyntaxError message has been printed the program execution ends.

Semantic errors

    Semantic error happens when the source code follows the grammatical rules of the language, but the Python interpreter can't understand what the programmer is trying to tell it to do.

    Usually semantic errors arise from a situation where the programmer tries some unknown operation or tries to refer to a variable or a function which does not exist.

    A couple of examples of semantic errors:

    print("Moon and Star" / 3.141593)

    Results the error message:

    Traceback (most recent call last):
      File "<test2.py>", line 1, in <module>
    TypeError: unsupported operand type(s) for /: 'str' and 'float'

    The reason being that Python has no idea how to divide text (i.e. a string) by a decimal number. Even as a human being with a superior brain capacity compared to Python, it is very hard to come up with an explanation what that expression could mean. Python just gives up.

    This command then:

    print(moonsugar)

    Results:

    Traceback (most recent call last):
      File "<test3.py>", line 1, in <module>
    NameError: name 'moonsugar' is not defined

    The reason of the failure is that the programmer is trying to use a variable named moonsugar but the variable does not exist: it has never been assigned a value. Python doesn't know what it is supposed to print on the screen. It could be fixed by assigning some useful value to moonsugar:

    moonsugar = "sweet"
    print(moonsugar)

    Unfortunately the error messages resulting from semantic errors are not as straightforward as the messages from SyntaxError. Usually though, if the error message does not contain the keyword SyntaxError it is pretty safe to assume it is a semantic error.

    Like with syntax errors the program execution ends after the error message has been printed.

Logical errors

    Logical errors are errors created by the programmer when designing the program's algorithm: the program works, but wrong i.e. it doesn't do what it is supposed to di.

    The only way to find out that a program has logical errors is to test it with different kinds of inputs and check it gives right results with all of them. The programming language can't really help with finding logical errors as it would require it to be able to read the programmers mind to know what he meant. From Python's point of view the wrongly working program is exactly what the programmer wanted.

At this point it is good to ask a question: what benefit is it to that there are different types of errors?

The benefit is that it helps the programmer to find and fix the error when she knows what kind of error is in question. For example the method of finding and fixing a logical error is quite different from doing the same with a syntax error.
Exercise about Finding and Fixing Errors in a Program

Let's apply what we learned above by fixing a program containing all the error types we now know about.

Create a new Python file and copy & paste the following program to PyCarm. Please use mouse to copy & paste to make sure there are no extra errors thanks to typos.

"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""

def main():
    age = input("Please, enter your age: ")

    if age < 25:
        ticket_price = 1.47
    elif age < 17:
        ticket_price = 1.02
    elif age < 7:
        ticket_price = 0.00
    else
        ticket_price = 2.04

    print(Your ride will cost: ticket_price)


if __name__ == "__main__":
    main()

Modify the program until it prints the ticket price correctly as defined in the initial comment.

(1) In reality there are more than three kinds, but we'll deal with them when and if the time comes.


'''