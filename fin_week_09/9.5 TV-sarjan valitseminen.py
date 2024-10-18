# COMP.CS.100 9.5 TV-sarjan valitseminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
rhis porgram does soemtingef
f
e
f

"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    parameter: filename
    return: dictTODO:
    """

    # TODO initialize a new data structure -DONE
    genre_dict = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            # TODO add the name and genres data to the data structure -DONE
            genre_dict[name] = genres

        file.close()
        return genre_dict # TODO return the data structure - DONE

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    # TODO print the genres

    unique_genres = set()

    print("Available genres are: ", end="")

    for name in sorted(genre_data):
        for i in range(len(genre_data[name])):
            unique_genres.update(genre_data[name])
            print(genre_data[name][i])

    print(sorted(unique_genres))
    print(", ".join(sorted(unique_genres)))

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series belonging to a genre.




if __name__ == "__main__":
    main()