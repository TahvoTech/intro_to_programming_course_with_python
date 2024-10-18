# COMP.CS.100 7.9 sanatiheyslaskuri
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
"""
program reads text and prints how many times a word is in the text and makes

example:

Enter rows of text for word counting. Empty row to quit.
I'm on a high way to hell
I'm on a high way to hell
It's going really well
Well it's only hell

a : 2 times
going : 1 times
hell : 3 times
high : 2 times
i'm : 2 times
it's : 2 times
on : 2 times
only : 1 times
really : 1 times
to : 2 times
way : 2 times
well : 2 times

"""

def main():

    print("Enter rows of text for word counting. Empty row to quit.")

    text = ""
    while True:
        row = input()
        if row == "":
            break
        else:
            text += " " + row.lower()

    list_of_words = text.split()
    sorted_list_of_words = sorted(list_of_words)
    words_dict = {}

    for i in range(len(sorted_list_of_words)):
        if sorted_list_of_words[i] not in words_dict:
            words_dict[sorted_list_of_words[i]] = 1
        elif sorted_list_of_words[i] in words_dict:
            words_dict[sorted_list_of_words[i]] = words_dict[sorted_list_of_words[i]] + 1



    for i in sorted(words_dict):
        print(f"{i} : {words_dict[i]} times")

if __name__ == "__main__":
    main()