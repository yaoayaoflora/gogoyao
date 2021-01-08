# Given a string, find the length of the longest substring in it with no more than K distinct characters.
def longest_substring_with_k_distinct(str1, k):
    windowStart = 0
    maxLength = 0
    charFreq = {}

    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar not in charFreq.keys():
            charFreq[rightChar] = 0
        charFreq[rightChar] += 1
        while len(charFreq) > k:
            leftChar = str1[windowStart]
            charFreq[leftChar] -= 1
            if charFreq[leftChar] == 0:
                del charFreq[leftChar]
            windowStart += 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()