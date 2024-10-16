# COMP.CS.100 1.6.8 Hymiöt Tervehdys main-funktiota käyttäen.
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
def main():

# Kysytään käyttäjältä mielialaa
    user_input = input("How do you feel? (1-10) ")
    mood = int(user_input)

# Tarkistetaan, onko syöte kelvollinen kokonaisluku
    if mood >= 1 and mood <= 10:
        if mood == 1:
            print("A suitable smiley would be :'(")
        elif mood == 10:
            print("A suitable smiley would be :-D")
        elif 4 <= mood <= 7:
            print("A suitable smiley would be :-|")
        elif mood > 7:
            print("A suitable smiley would be :-)")
        else:
            print("A suitable smiley would be :-(")
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()