# COMP.CS.100 6.9 Yhden rivin ROT-13-salaus
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program encrypts text

Example of the program in use:

>> encrypt("e")
'r'
>> encrypt("E")
'R'
>> encrypt("?")
'?'
>> row_encryption("Happy, happy, joy, joy!")
'Unccl, unccl, wbl, wbl!'

"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]


    regular_chars_str = ""
    for i in range(len(regular_chars)):
        regular_chars_str = regular_chars_str + regular_chars[i]

    encrypted_chars_str = ""
    for i in range(len(encrypted_chars)):
        encrypted_chars_str = encrypted_chars_str + encrypted_chars[i]

    regular_chars_str = regular_chars_str + regular_chars_str.upper()
    encrypted_chars_str = encrypted_chars_str + encrypted_chars_str.upper()

    lista = ""

    for i in range(len(text)):
        if text[i] in regular_chars_str:
            lista = lista + encrypted_chars_str[regular_chars_str.find(text[i])]
        else:
            lista = lista + text[i]

    return lista

def row_encryption(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]


    regular_chars_str = ""
    for i in range(len(regular_chars)):
        regular_chars_str = regular_chars_str + regular_chars[i]

    encrypted_chars_str = ""
    for i in range(len(encrypted_chars)):
        encrypted_chars_str = encrypted_chars_str + encrypted_chars[i]

    regular_chars_str = regular_chars_str + regular_chars_str.upper()
    encrypted_chars_str = encrypted_chars_str + encrypted_chars_str.upper()

    lista = ""

    for i in range(len(text)):
        if text[i] in regular_chars_str:
            lista = lista + encrypted_chars_str[regular_chars_str.find(text[i])]
        else:
            lista = lista + text[i]


    return lista

def main():

#    encrypt("eeffe")
#    encrypt("E")
#    encrypt("?")
#    encrypt("Happy, happy, joy, joy!")
    row_encryption("Happy, happy, joy, joy!")


if __name__ == "__main__":
    main()