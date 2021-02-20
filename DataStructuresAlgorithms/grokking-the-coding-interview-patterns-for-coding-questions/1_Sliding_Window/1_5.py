# Given a string, find the length of the longest substring which has no repeating characters.


def non_repeat_substring(str1):
    startIndex = 0
    maxLength = 0
    charIndex = {}

    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar in charIndex:
            startIndex = max(startIndex, charIndex[rightChar] + 1)
        charIndex[rightChar] = endIndex
        maxLength = max(maxLength, endIndex - startIndex + 1)
    
    return maxLength


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()