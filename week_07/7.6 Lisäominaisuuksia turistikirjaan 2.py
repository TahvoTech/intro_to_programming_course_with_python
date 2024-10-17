# COMP.CS.100 7.6 Lisäominaisuuksia turistikirjaan 1
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program is a spanish english dictionary wehre you can ask word, add, remove,
print, trlansate sencentes and quit with actions.

with worods it included to be shown in the beginning.

"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")
    content = ", ".join(sorted(english_spanish))
    print(content)

    while True:



        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            elif word not in english_spanish:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
#            english_spanish[input("Anna avain: ")] = input("Anna arvo: ")
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[english_word] = spanish_word
            print("Dictionary contents:")
            content = ", ".join(sorted(english_spanish))
            print(content)
        elif command == "R":
            rem_word = input("Give the word to be removed: ")
            if rem_word in english_spanish:
                del english_spanish[rem_word]
            elif rem_word not in english_spanish:
                print("The word hey could not be found from the dictionary.")

        elif command == "P":


            spanish_english = {}
            for i in english_spanish:
                spanish_english[english_spanish[i]] = i

            print()
            print("English-Spanish")
            for key in sorted(english_spanish):
                print(key, english_spanish[key])
            print()
            print("Spanish-English")
            for key in sorted(spanish_english):
                print(key, spanish_english[key])
            print()

        elif command == "T":

            text = input("Enter the text to be translated into Spanish: ")

            print(f"The text, translated by the dictionary:")

            words_in_text = text.split()

            translated_text_list = []
            for i in range(len(words_in_text)):
                if words_in_text[i] in english_spanish:
                    translated_text_list.append(english_spanish[words_in_text[i]])
                elif words_in_text[i] not in english_spanish:
                    translated_text_list.append(words_in_text[i])

            translated_text_str = " ".join(translated_text_list)

            print(translated_text_str)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()