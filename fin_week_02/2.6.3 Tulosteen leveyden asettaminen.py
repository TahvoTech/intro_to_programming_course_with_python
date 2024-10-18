# COMP.CS.100 2.6.3 Tulosteen leveyden asettaminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
ohjelma, joka tulostaa yksinkertaisen lunttilapun kertotaulun opettelemista
varten. Muotoile ohjelman tuloste siten, että jokainen kertolaskun tulos
näytetään neljän merkin levyisessä tulostuskentässä. Ohjelman tulosteen
pitää siis näyttää seuraavalta:

 1   2   3   4   5   6   7   8   9  10
 2   4   6   8  10  12  14  16  18  20
 3   6   9  12  15  18  21  24  27  30
 4   8  12  16  20  24  28  32  36  40
 5  10  15  20  25  30  35  40  45  50
 6  12  18  24  30  36  42  48  54  60
 7  14  21  28  35  42  49  56  63  70
 8  16  24  32  40  48  56  64  72  80
 9  18  27  36  45  54  63  72  81  90
10  20  30  40  50  60  70  80  90 100
Neuvoja tehtävän tekemiseen:

Koodipohjassa on käytetty for-silmukkaa, jonka sisällä on toinen for-silmukka.
Mikäli tämän toiminta ei ole selvää, kannattaa lukea kohdan 2.8 materiaali
ennen kuin aloitat tehtävän tekemisen.

Huomaathan, että koska tässä tehtävässä harjoitellaan juurikin
välilyöntien tulostamista, niin automaattinen arviointi tarkastaa erityisesti
välilyöntien määrän, jonka pitää olla täsmälleen oikea.

"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()

