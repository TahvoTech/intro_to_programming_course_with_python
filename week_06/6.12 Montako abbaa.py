# COMP.CS.100 6.12 Montako abbaa
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program is a decrypting program

Example of the program in use:

>> count_abbas("abbabbabba")
3
>> count_abbas("barbapapa")
0
"""

def count_abbas(text):
    """
    function counts "abba"'s in the given text
    """
#    print(text)
    counter = 0
    for i in range(len(text)):
        if text[i] == "a":
#            print(text[i:i+4])
            if text[i:i+4] == "abba":
                counter += 1
#    print(counter)
    return counter
def main():

    count_abbas("abbabbabba")
#    count_abbas("barbapapa")


if __name__ == "__main__":
    main()