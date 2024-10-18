# COMP.CS.100 6.10 Viestin tallentaminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program asks for message and returns it in capital

Example of the program in use:

Enter text rows to the message. Quit by entering an empty row.
Puff, the magic dragon lived by the sea,
And frolicked in the autumn mist, in a land called Honah Lee.

The same, shouting:
PUFF, THE MAGIC DRAGON LIVED BY THE SEA,
AND FROLICKED IN THE AUTUMN MIST, IN A LAND CALLED HONAH LEE.

"""

def read_message(text):
    """
    function makes a list of inputs
    """
    list_of_messages = [text]

    while True:
        message = input()
        if message != "":
            list_of_messages.append(message)
        else:
            break

    return list_of_messages

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message(input())

    print("The same, shouting:")
    for i in range(len(msg)):
        print(msg[i].upper())


if __name__ == "__main__":
    main()