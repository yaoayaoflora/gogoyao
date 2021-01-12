# Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str1, k):
    startIndex = 0
    maxLength = 0
    charFrequency = {}

    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar not in charFrequency:
            charFrequency[rightChar] = 0
        charFrequency[rightChar] += 1

        while len(charFrequency) > k:
            leftChar = str1[startIndex]
            startIndex += 1
            charFrequency[leftChar] -= 1
            if charFrequency[leftChar] == 0:
                del charFrequency[leftChar]
        
        maxLength = max(maxLength, endIndex - startIndex + 1)
    
    return maxLength

def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()