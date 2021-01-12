# Given a string and a pattern, find all anagrams of the pattern in the given string.

def find_string_anagrams(str1, pattern):
    startIndex = 0
    matched = 0
    charFreqToMatch = {}
    resultIndices = []

    for char in pattern:
        if char not in charFreqToMatch:
            charFreqToMatch[char] = 0
        charFreqToMatch[char] += 1
    
    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar in charFreqToMatch:
            charFreqToMatch[rightChar] -= 1
            if charFreqToMatch[rightChar] == 0:
                matched += 1
        
        if matched == len(charFreqToMatch):
            resultIndices.append(startIndex)
        
        if endIndex >= len(pattern) - 1:
            leftChar = str1[startIndex]
            startIndex += 1
            if leftChar in charFreqToMatch:
                if charFreqToMatch[leftChar] == 0:
                    matched -= 1
                charFreqToMatch[leftChar] += 1
        
    return resultIndices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()