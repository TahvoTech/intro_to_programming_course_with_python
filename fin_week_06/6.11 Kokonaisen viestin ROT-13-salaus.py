# COMP.CS.100 6.11 Kokonaisen viestin ROT-13-salaus
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program is a decrypting program

Example of the program in use:

Enter text rows to the message. Quit by entering an empty row.
Puff, the magic dragon lived by the sea,
And frolicked in the autumn mist, in a land called Honah Lee.

ROT13:
Chss, gur zntvp qentba yvirq ol gur frn,
Naq sebyvpxrq va gur nhghza zvfg, va n ynaq pnyyrq Ubanu Yrr.

"""

def read_message():
    """
    Lukee käyttäjältä syötettä, kunnes tyhjä rivi syötetään, ja tallentaa rivit listaan.

    :param: none
    :return: Lista, joka sisältää käyttäjän syöttämät rivit.
    """
    messages = []
    while True:
        message = input()
        if message == "":
            break
        messages.append(message)
    return messages

def encrypt(char):
    """
    Suorittaa ROT13-muunnoksen yhdelle merkille.

    :param: str, muunnettava merkki
    :return: str, salattu merkki
    """
    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if char.isalpha():
        if char.isupper():
            return encrypted_chars[regular_chars.index(char.lower())].upper()
        else:
            return encrypted_chars[regular_chars.index(char)]
    return char

def row_encryption(message):
    """
    Suorittaa ROT13-muunnoksen kokonaiselle merkkijonolle.

    :param: str, muunnettava teksti
    :return: str, salattu teksti
    """
    result = ""
    for char in message:
        result = result + encrypt(char)

    return result

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    messages = read_message()

    print("ROT13:")
    for message in messages:
        print(row_encryption(message))


if __name__ == "__main__":
    main()