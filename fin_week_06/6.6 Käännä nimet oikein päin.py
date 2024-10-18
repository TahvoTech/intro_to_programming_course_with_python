# COMP.CS.100 6.6 Käännä nimet oikein päin
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program transforms names to correct form ("firstname surname") when a input
is first "surname, firstname". It also strips every excess spaces in front
and end of the input and also deletes "," in the input.

Example of the program in use:

>> reverse_name("Techie, Teddy")
'Teddy Techie'
>> reverse_name("Scumble,    Arnold")
'Arnold Scumble'
>> reverse_name("Fortunato,Frank")
'Frank Fortunato'
>> reverse_name("von Grünbaumberger, Herbert")
'Herbert von Grünbaumberger'
>> reverse_name("   Duck,     Donald  ")
'Donald Duck'
"""


def reverse_name(fullname):
    """
    function takes in a string that is a name. If name has "," in it,
    it is expected to have both first and surname, but in wrong order. This
    function reverses the order so that the first name is first and surname
    last and no comma.

    :param: str, fullname
    :return: no return
    """
    fullname_list = fullname.split(",")
    if "," in fullname:
        firstname = str(fullname_list[1].strip())
        surname = str(fullname_list[0].strip())
        if len(firstname) <= 0:
            return surname
        elif len(surname) <= 0:
            return firstname
        elif len(firstname) > 0 and len(surname) > 0:
            fullname = firstname + " " + surname
            return fullname
    else:
        return fullname

def main():
    reverse_name("Techie, Teddy")
    reverse_name("Scumble,    Arnold")
    reverse_name("Fortunato,Frank")
    reverse_name("von Grünbaumberger, Herbert")
    reverse_name("   Duck,     Donald  ")
    reverse_name("X,")
    reverse_name(",X")
    reverse_name(" , Y ")
    reverse_name(",")
    reverse_name("Stuart Student")
    reverse_name("Mando")


if __name__ == "__main__":
    main()
