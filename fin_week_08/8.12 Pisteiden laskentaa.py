# COMP.CS.100 8.12 Pisteiden laskentaa
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

""" This script reads a file containing scores for various contestants,
sums up the scores for each contestant if they appear multiple times,
and then prints the aggregated scores in alphabetical order by the contestant's name.
"""

def main():
    # Prompt the user to enter the name of the score file
    file_name = input("Enter the name of the score file: ")

    try:
        # Open the specified file in read mode
        file = open(file_name, mode="r")

        # Initialize an empty dictionary to hold the aggregated scores for each contestant
        gamers = {}
        print("Contestant score:")

        # Read each line of the file


        for file_line in file:
            # Split the line into name and score, assuming a space separates them
            try:
                name, score_str = file_line.split()
                # Convert the score from a string to an integer
                try:
                    score_int = int(score_str)

                    # Check if the contestant's name is already in the dictionary
                    if name not in gamers:
                        # If not, add the name and score to the dictionary
                        gamers[name] = score_int
                    else:
                        # If the name is already in the dictionary, add the new score to the existing score
                        gamers[name] += score_int
                except OSError:
                    print("There was an erroneous score in the file:")
                    print(score_str)
            except OSError:
                print("There was an erroneous line in the file:")
                print(file_line)
        # Close the file after reading all lines
        file.close()


        # Print the aggregated scores for each contestant, sorted alphabetically by name
        for i in sorted(gamers):
            print(i, gamers[i])

    except OSError:
        print("There was an error in reading the file.")

# Ensures that the main function is called only when this script is executed directly,
# and not when imported as a module in another script
if __name__ == "__main__":
    main()

