# COMP.CS.100 2.6.1 Tulostarkkuuden asettaminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
ensimmäisessä kohdassa piin likiarvo tulostetaan nollan desimaalin
tarkkuudella (eli kokonaislukuna) ja toisessa kohdassa neljän desimaalin
tarkkuudella. Ohjelman tulosteen pitää siis näyttää seuraavalta:

Esimerkki ohjelman toiminnasta:

The approximate value of pi is 3 or, if we want to get specific, 3.1416

"""

def main():
    PI = 3.14159265358979323846
    print(f"The approximate value of pi is {PI:.0f} or, if we want to get specific, {PI:.4f}")

if __name__ == "__main__":
    main()
