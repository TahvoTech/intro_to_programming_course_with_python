# COMP.CS.100 1.6.9 Kivi-paperi-sakset.
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
def main():

# https://plus.tuni.fi/comp.cs.100/2023-2024/rounds_01/01_peruskasitteet/01_exercises_vaihtorahat_assignment/?hl=fi
# Kirjoita ohjelma, joka kysyy ostosten hinnan ja millä rahalla maksetaan ja
# tulostaa, minkälaisia vaihtorahoja pitää antaa.
# Yksinkertaistetaan ohjelmaa niin, että käytössä ei ole
# kuin 1, 2, 5 ja 10 euron rahoja ja kokonaishinta on aina tasaeuroja.
# Tehtävässä oletetaan myös, että ostosten hinta on vähintään 1 euro.

# Aloitetaan ohjelma input komennon hyödyntämisellä, joka kysyy ostosten hinnan ja millä rahalla maksetaan.

    purchase_price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))

    change = paid_amount - purchase_price

#    print(change)
#    tens = change // 10
#    print(tens)
#    fives = change // 5
#    print(fives)
#    twos = change // 2
#    print(twos)
#    ones = change // 1
#    print(ones)
    tens = change // 10
    fives = (change % 10) // 5
    twos = (change % 10 % 5) // 2
    ones = (change % 10 % 5 % 2) // 1


    if change <= 0:
        print("No change")
    else:
        print("Offer change:")
        if tens >= 1:
            print(tens, "ten-euro notes")
        if fives >= 1:
            print(fives, "five-euro notes")
        if twos >= 1:
            print(twos, "two-euro coins")
        if ones >= 1:
            print(ones, "one-euro coins")


if __name__ == "__main__":
    main()