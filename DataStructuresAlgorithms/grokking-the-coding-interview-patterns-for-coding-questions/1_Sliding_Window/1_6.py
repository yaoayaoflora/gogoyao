# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’
# letters with any letter, find the length of the longest substring having the same letters after
# replacement.

def length_of_longest_substring(str1, k):
    startIndex = 0
    maxLength = 0
    maxRepeatCharCount = 0
    charsFrequency = {}

    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar not in charsFrequency:
            charsFrequency[rightChar] = 0
        charsFrequency[rightChar] += 1
        maxRepeatCharCount = max(maxRepeatCharCount, charsFrequency[rightChar])

        if endIndex - startIndex + 1 - maxRepeatCharCount > k:
            leftChar = str1[startIndex]
            startIndex += 1
            charsFrequency[leftChar] -= 1
        
        maxLength = max(maxLength, endIndex - startIndex + 1)

    return maxLength
    

def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()