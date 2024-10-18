"""
COMP.CS.100 Ohjelmointi 1, syksy 2023, luento 2.
Tekijä: Jorma Laurikkala
Opiskelijanumero: ---------
Luetaan ja tulostetaan arvosana.
Versio 5: lisätty pääsilmukka.
"""

def main():
    # Alustetaan pääsilmukkaa ohjaava lippu siten,
    # että silmukka saadaan käytiin.
    jatketaan = True

    # Kysellään arvosanoja kunnes käyttäjä kyllästyy.
    while jatketaan:
        # Luetaan syöte käyttäjältä.
        syöte = input("Anna arvosana tai kirjoita \"lopeta\": ")

        # Varsinainen arvosanan lausunta on ehdon takana,
        # koska lopettavaa syötettä ei voi muuntaa kokonaisluvuksi.
        if syöte != "lopeta":
            # Muunnetetaan syöte kokonaisluvuksi, jotta vertailu ja
            # aritmetiikka onnistuu.
            arvosana = int(syöte)

            # Tulostetaan arvosana näytölle hienommin.
            if arvosana == 1:
                print("Arvosanasi on välttävä.")
            elif arvosana == 2:
                print("Arvosanasi on tyydyttävä.")
            elif arvosana == 3:
                print("Arvosanasi on hyvä.")
            elif arvosana == 4:
                print("Arvosanasi on kiitettävä.")
            elif arvosana == 5:
                print("Arvosanasi on erinomainen.")
            else:
                print("Virheellinen arvosana!")

            # Pohditaan mitä arvosana olisi yhdellä korotettuna,
            # jos voidaan korottaa. Valintarakenne varmistaa,
            # että virheellistä tai kiitettävää arvosanaa ei
            # koroteta.
            if arvosana >= 1:
                if arvosana < 5:
                    arvosana = arvosana + 1
                    print("Yhdellä korotettu arvosana on", arvosana)

        # Käännetään lippu.
        else:
            jatketaan = False

if __name__ == "__main__":
    # Kutsutaan pääohjelmaa.
    main()
