# COMP.CS.100 5.3.2 Listan alkioiden läpikäyminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Tee ohjelma, joka lukee ensin 5 kpl käyttäjän syöttämiä lukuja listaan ja tulostaa sitten kaikki syötetyt luvut päinvastaisessa järjestyksessä. Esimerkki ohjelman toiminnasta:

Give 5 numbers:
Next number: 2
Next number: 7
Next number: 3
Next number: -8
Next number: 6
The numbers you entered, in reverse order:
6
-8
3
7
2
"""

def main():

    print("Give 5 numbers:")
    numbers = []

    for i in range(5):
        numbers.append(int(input("Next number: ")))

    print("The numbers you entered, in reverse order:")
    for i in reversed(numbers):
        print(i)

if __name__ == "__main__":
    main()