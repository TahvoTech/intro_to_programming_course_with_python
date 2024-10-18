# COMP.CS.100
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

'''
Kirjoita ohjelma, joka kysyy käyttäjältä opintotuen suuruuden ja laskee, miten 1.17 prosentin indeksikorotus vaikuttaa opintotukeen. Ohjelma tulostaa seuraavasti:

    Enter the amount of the study benefits: 335.32
    If the index raise is 1.17 percent, the study benefit,
    after a raise, would be 339.243244 euros

Neuvoja tehtävän tekemiseen:

    Tarvitset ohjelmaasi muuttujan käyttäjän syötteen tallentamista varten. Huomaa nyt myös, että käyttäjän syöte on tietotyypiltään merkkijono ja sinun pitää ohjelmassasi muuttaa se liukuluvuksi.

    Pohdi, kannattaisiko myös indeksikorotusprosentin arvo tallettaa muuttujaan.

    Huomaa, että ohjelman tuloste on jaettu useammalle riville. Automaattitarkastus ei välitä välimerkeistä, mutta rivijako on merkityksellinen, eli muotoile ohjelmasi tulosteen rivijako samoin kuin esimerkkiajossa.

    Voit laskea korotetun opintotuen suuruuden kertolasku-operaattoria käyttäen ja tallentaa sen joko samaan muuttujaan tai tehdä uuden muuttujan uuden arvon tallentamista varten. Onko parempi käyttää samaa muuttujaa vai tehdä uusi muuttuja?

    Kokeile myös, mitä tapahtuu, jos ohjelmaa testatessasi syötät desimaalipisteen sijaan desimaalipilkun.

b)

Ollaan optimistisia tulevaisuuden suhteen ja lisätään ohjelmaan vielä toisenkin indeksikorotuksen laskeminen. Nyt ohjelma tulostaa seuraavasti:

    Enter the amount of the study benefits: 335.32
    If the index raise is 1.17 percent, the study benefit,
    after a raise, would be 339.243244 euros
    and if there was another index raise, the study
    benefits would be as much as 343.2123899548 euros

Tehtävää tehdessäsi pohdi:

    Olivatko a-kohdassa tekemäsi ratkaisut hyviä vai huonoja b-kohdan toteuttamisen kannalta? Miksi/miksi ei?
'''

benefits = float(input("Enter the amount of the study benefits: "))
increase = 1.0117
raised_benefits = benefits*increase

print(f"If the index raise is {increase} percent, the study benefit,\nafter a raise, would be {raised_benefits} euros")