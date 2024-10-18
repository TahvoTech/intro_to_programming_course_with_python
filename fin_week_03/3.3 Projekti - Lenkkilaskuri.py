# COMP.CS.100 3.3 Projekti: Lenkkilaskuri
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

def main():

    # Kysytään käyttäjältä seurattavien päivien lukumäärä
    num_of_days = int(input("Enter the number of days: "))

    # Alustetaan tarvittavat muuttujat
    total_distance = 0
    lazy_days = 0

    # Käydään läpi kunkin päivän lenkkimatka
    for day in range(1, num_of_days + 1):
        distance = float(input(f"Enter day {day} running length: "))

        # Lisätään matka yhteen
        total_distance += distance

        # Tarkistetaan, onko kolme peräkkäistä päivää nollaa
        if distance == 0:
            lazy_days += 1
            if lazy_days == 3:
                print("You had too many consecutive lazy days!")
                break
        else:
            lazy_days = 0  # Nollataan laiskat päivät laskuri

    # Lasketaan keskiarvo
    if num_of_days > 0:
        mean_distance = total_distance / num_of_days
    else:
        mean_distance = 0

    # Tulostetaan tulokset kahden desimaalin tarkkuudella
    if mean_distance < 3.00:
        print(f"Your running mean of {mean_distance:.2f} km was too low!")
    else:
        print(f"You were a persistent runner! With a mean of {mean_distance:.2f} km.")


if __name__ == "__main__":
    main()
    