# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’
# letters with any letter, find the length of the longest substring having the same letters after
# replacement.

def length_of_longest_substring(str1, k):
    start = 0
    maxLength = 0
    maxRepeatLetterCount = 0
    charFreq = {}

    for end in range(len(str1)):
        right = str1[end]
        if right not in charFreq:
            charFreq[right] = 0
        charFreq[right] += 1
        maxRepeatLetterCount = max(maxRepeatLetterCount, charFreq[right])
        if (end - start + 1 - maxRepeatLetterCount) > k:
            left = str1[start]
            charFreq[left] -= 1
            start += 1
        maxLength = max(maxLength, end - start + 1)
    
    return maxLength


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()