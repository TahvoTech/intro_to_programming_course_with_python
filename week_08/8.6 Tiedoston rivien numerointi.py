# COMP.CS.100 8.6 Tiedoston rivien numerointi
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
This script reads lines from a file named 'text.txt', strips trailing newline characters from each line,
and prints each line prefixed with its line number. The line numbers start from 1 and increment for each line.

The script demonstrates basic file reading and line numbering in Python without using the built-in enumerate function.
"""

def main():

    file_name = input("Enter the name of the file: ")

    # Open the file in read mode.
    file = open(file_name, mode="r")

    round = 1  # Initialize the line number counter.
    for file_line in file:
        file_line = file_line.rstrip()  # Remove trailing newline characters.
        print(round, file_line)  # Print the line number and the line.
        round += 1  # Increment the line number counter.

    file.close()  # Close the file.

if __name__ == "__main__":
    main()
