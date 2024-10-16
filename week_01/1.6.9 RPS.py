# COMP.CS.100 1.6.9 Kivi-paperi-sakset.
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
def main():

# https://plus.tuni.fi/comp.cs.100/2023-2024/rounds_01/01_peruskasitteet/01_exercises_kivi_paperi_sakset_assignment/


# Aloitetaan ohjelma input komennon hyödyntämisellä, jotta saadaan kahden pelaajan vastaukset.

    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")

    if player_1 == "R" and player_2 == "P" :
        print("Player 2 won!")
    elif player_1 == "P" and player_2 == "S":
        print("Player 2 won!")
    elif player_1 == "S" and player_2 == "R":
        print("Player 2 won!")
    elif player_1 == player_2:
        print("It's a tie!")
    else:
        print("Player 1 won!")
if __name__ == "__main__":
    main()