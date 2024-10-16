# COMP.CS.100 2.3.1 kertotaulu kouluversio
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
example:

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
10 * 6 = 60

"""

def main():

    repetition_counter = 1
    chosen_number = int(input("Choose a number: "))

    while repetition_counter <= 10:
        print(repetition_counter, "*", chosen_number, "=", chosen_number * repetition_counter)
        repetition_counter += 1

if __name__ == "__main__":
    main()