# Given a word, write a function to generate all of its unique generalized abbreviations.
# 
# Generalized abbreviation of a word can be generated by replacing each substring of the word by the count of characters 
# in the substring. Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After replacing these 
# substrings in the actual word by the count of characters we get all the generalized abbreviations: 
# “ab”, “1b”, “a1”, and “2”.


def generate_generalized_abbreviation(word):
    result = []
    generate_abbreviation_recursive(word, list(), 0, 0, result)
    return result


def generate_abbreviation_recursive(word, abWord, start, count, result):
    if start == len(word):
        if count != 0:
            abWord.append(str(count))
        result.append(''.join(abWord))
    else:
        # continue abbreviating by incrementing the current abbreviation count
        generate_abbreviation_recursive(
            word, list(abWord), start + 1, count + 1, result)

        # restart abbreviating, append the count and the current character to the string
        if count != 0:
            abWord.append(str(count))
        newWord = list(abWord)
        newWord.append(word[start])
        generate_abbreviation_recursive(word, newWord, start + 1, 0, result)


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()