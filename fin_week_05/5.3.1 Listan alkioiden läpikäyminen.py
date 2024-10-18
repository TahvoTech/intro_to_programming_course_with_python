# COMP.CS.100 5.3.1 Listan alkioiden läpikäyminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
ohjelma lukee ensin 5 kpl käyttäjän syöttämiä lukuja ja sitten tulostaa
syöttämisjärjestyksessä kaikki nollaa suuremmat luvut. Esimerkki ohjelman
toiminnasta:


Give 5 numbers:
Next number: 0
Next number: 1
Next number: -2
Next number: 3
Next number: -4
The numbers you entered that were greater than zero were:
1
3

"""

def main():

    print("Give 5 numbers:")
    numbers = []

    for i in range(5):
        numbers.append(int(input("Next number: ")))
    print("The numbers you entered that were greater than zero were:")
    for numbers_over_0 in numbers:
        if numbers_over_0 > 0:
            print(numbers_over_0)

if __name__ == "__main__":
    main()