# COMP.CS.100 2.6.2 Tulosteen välilyönnit kuntoon
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
ohjelma, joka kysyy käyttäjän nimen ja tervehtii sitten häntä
alla olevassa esimerkkiajossa esitetyllä tekstillä.
Tarkoituksena on, että tuloste muotoillaan täsmälleen esimerkkitulosteessa
esitetyllä tavalla, eli käyttäjän nimen jälkeen tulostettava pilkku tulee
kiinni nimeen ilman, että nimen ja pilkun välissä olisi välilyöntiä.

Esimerkki ohjelman toiminnasta:

Tell us your name: Teemu
Hey Teemu, the printout formatting is going well!

"""

def main():

    name = input("Tell us your name: ")
    print(f"Hey {name}, the printout formatting is going well!")

if __name__ == "__main__":
    main()
