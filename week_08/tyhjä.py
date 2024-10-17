# COMP.CS.100 8.13 pisteiden laskennan virhetilanteet
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

""" This script reads a file containing scores for various contestants,
sums up the scores for each contestant if they appear multiple times,
and then prints the aggregated scores in alphabetical order by the contestant's name.
"""

def main():
    hakemisto = {}
    print("Syötä sana ja sivunumero (lopeta tyhjällä rivillä):")
    while True:
        rivi = input()
        if rivi == "":
            break

        tiedot = rivi.split()
        hakusana = tiedot[0]
        sivunumero = int(tiedot[1])

        if hakusana not in hakemisto:
            hakemisto[hakusana] = []
        hakemisto[hakusana].append(sivunumero)

    print(hakemisto)
    for sana in sorted(hakemisto):
        print(sana, "", end="")
        for numero in sorted(hakemisto[sana]):
            print(numero, "", end="")
        print()


if __name__ == "__main__":
    main()