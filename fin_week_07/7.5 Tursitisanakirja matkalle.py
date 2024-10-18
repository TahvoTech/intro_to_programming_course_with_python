# COMP.CS.100 7.5 Turistisanakirja
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program is a spanish english dictionary wehre you can ask word, add, remove,
print, trlansate sencentes and quit with actions.

"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

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

        elif command == "R":
            rem_word = input("Give the word to be removed: ")
            if rem_word in english_spanish:
                del english_spanish[rem_word]
            elif rem_word not in english_spanish:
                print("The word hey could not be found from the dictionary.")

        elif command == "P":
            for key in sorted(english_spanish):
                print(key, english_spanish[key])

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