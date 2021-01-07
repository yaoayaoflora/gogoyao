# Given a string, find the length of the longest substring which has no repeating characters.
def non_repeat_substring(str1):
    start = 0
    maxLength = 0
    charIndex = {}

    for end in range(len(str1)):
        right = str1[end]
        if right in charIndex:
            start = max(start, charIndex[right] + 1)
        charIndex[right] = end
        maxLength = max(maxLength, end - start + 1)
    
    return maxLength


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()