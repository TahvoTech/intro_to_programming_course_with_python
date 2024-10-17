# COMP.CS.100 6.13 Pisin järjestetty alimerkkijono
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
program returnsn the longest substring in order from the given text.

ecamplee:

>> longest_substring_in_order("abcabcdefgabab")
'abcdefg'
>> longest_substring_in_order("acdkbarstyefgioprtyrtyx")
'efgioprty'

"""

def longest_substring_in_order(text):
    """
    function finds the longest substring in order from the given text.
    """
    # if length is 0 or 1, empty or only one letter, the funktion should
    # return just that.
    if len(text) <= 1:
        return text

    # we start with the first letters instead of empty strings
    longest = text[0]
    current = text[0]

    for index in range(1, len(text)):
        if text[index] >= text[index-1]:
            current += text[index]
            if len(current) > len(longest):
                longest = current
        else:
            current = text[index]

    return longest

def main():
    longest_substring_in_order("abcabc")
#    longest_substring_in_order("abcabcdefgabab")
#    longest_substring_in_order("acdkbarstyefgioprtyrtyx")


if __name__ == "__main__":
    main()