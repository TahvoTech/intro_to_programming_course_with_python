# COMP.CS.100 5.4.1 Montako löytyy
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
 funktio input_to_list, joka saa parametrinaan tiedon siitä, kuinka monta lukua halutaan lukea, kertoo käyttäjälle, että nyt syötetään parametrin verran lukuja, lukee luvut käyttäjältä, tallentaa ne listaan ja palauttaa tämän listan.

Tee myös pääohjelma, joka:

kysyy käyttäjältä käsiteltävien lukujen lukumäärän
kutsuu edellä määriteltyä funktiota lukeakseen käyttäjältä lukuja
kysyy käyttäjältä, mitä lukua etsitään
tulostaa tiedon siitä, löytyykö etsitty luku syötettyjen lukujen joukosta ja jos, niin kuinka monta kertaa
Esimerkkejä ohjelman toiminnasta (funktion input_to_list vastuulla ovat rivit 2–7):

1
2
3
4
5
6
7
8
9
How many numbers do you want to process: 5
Enter 5 numbers:
7
3
2
7
7
Enter the number to be searched: 7
7 shows up 3 times among the numbers you have entered.
Seuraavassa esimerkissä rivit 2–5 tapahtuvat input_to_list-funktiossa:

1
2
3
4
5
6
7
How many numbers do you want to process: 3
Enter 3 numbers:
5
6
7
Enter the number to be searched: 3
3 is not among the numbers you have entered.

"""

def input_to_list(numbers):
    """
    function adds numbers to a list and returns the list.

    :param: int, amount of numbers to be added.
    :return: list, list of numbers added to the list.
    """
    list_of_numbers = []

    print(f"Enter {numbers} numbers:")

    for i in range(numbers):
        list_of_numbers.append(int(input()))

    return list_of_numbers

def find_number(find_this, list_of_numbers):
    """
    function finds how many times a specific numbers can be found in the list.

    :param: int, find_this, the number that the coders wants to find.
    :param: list, list_of_numbers, this is a list made before and is used to
    check if the specific nuimber is found in the liest and how many times.
    :return: int, number of times the number is found in the list.
    """
    found_match = 0
    for i in range(len(list_of_numbers)):
        if find_this == list_of_numbers[i]:
            found_match += 1
    return found_match

def main():

    amount_of_numbers = int(input("How many numbers do you want to process: "))
    list_of_numbers = input_to_list(amount_of_numbers)
    find_this_number = int(input("Enter the number to be searched: "))
    found_match = find_number(find_this_number, list_of_numbers)
    if found_match > 0:
        print(f"{find_this_number} shows up {found_match} times among the "
              f"numbers you have entered.")
    else:
        print(f"{find_this_number} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()