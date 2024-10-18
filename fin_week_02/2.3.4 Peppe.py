"""
Draws PEPPE based on user's choices.
"""

def main():
    # Print information to the user.
    print("Hello! I draw letter E with a center line.")

    # Read the drawing character.
    char = input("Please, enter the drawing character: ")

    # Read the height of the letter and convert the input to an integer.
    height_as_string = input("Please, enter the height of the drawing: ")
    height = int(height_as_string)

    # Draw if the height is odd and greater than or equal to 3 characters.
    if height % 2 == 1 and height >= 3:
        # Calculate the number of spaces before and after the character.
        nspaces = (height - 1) // 2

        print("")

        # Print the top horizontal line of the "E" letter.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char + " " * (int((height) - 2)) + char)

        # Print the center horizontal line.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char)

        # Print the bottom horizontal line of the "E" letter.
        print(char)

        print("")

        # Print the top horizontal line of the "E" letter.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char)

        # Print the center horizontal line.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char)

        # Print the bottom horizontal line of the "E" letter.
        print(char * height)

        print("")


        # Print the top horizontal line of the "E" letter.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height - 1) / 2)):
            print(char + " " * (int((height) - 2)) + char)

        # Print the center horizontal line.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height - 1) / 2)):
            print(char)

        # Print the bottom horizontal line of the "E" letter.
        print(char)

        print("")
        # Print the top horizontal line of the "E" letter.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height - 1) / 2)):
            print(char + " " * (int((height) - 2)) + char)

        # Print the center horizontal line.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height - 1) / 2)):
            print(char)

        # Print the bottom horizontal line of the "E" letter.
        print(char)

        print("")

        # Print the top horizontal line of the "E" letter.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char)

        # Print the center horizontal line.
        print(char * height)

        # Print the vertical line of the "E" letter.
        for ind in range(1, int((height-1)/2)):
            print(char)

        # Print the bottom horizontal line of the "E" letter.
        print(char * height)


    else:
        print("Invalid height!")

if __name__ == "__main__":
    main()
