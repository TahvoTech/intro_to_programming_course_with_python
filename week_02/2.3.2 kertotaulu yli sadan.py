# COMP.CS.100 2.3.2 kertotaulu yli sadan
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
example:

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
17 * 6 = 102

"""

def main():

    repetition_counter = 1
    chosen_number = int(input("Choose a number: "))
    cumulative_value = 0

    while cumulative_value <= 100:
        cumulative_value = chosen_number * repetition_counter
        print(repetition_counter, "*", chosen_number, "=", cumulative_value)
        repetition_counter += 1

if __name__ == "__main__":
    main()