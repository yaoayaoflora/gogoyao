# Given a string and a pattern, find all anagrams of the pattern in the given string.

def find_string_anagrams(str1, pattern):
    startIndex = 0
    matched = 0
    anagrams = []
    charFreq = {}

    for char in pattern:
        if char not in charFreq:
            charFreq[char] = 0
        charFreq[char] += 1
    
    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar in charFreq:
            charFreq[rightChar] -= 1
            if charFreq[rightChar] == 0:
                matched += 1
        
        if matched == len(charFreq):
            anagrams.append(startIndex)

        if endIndex >= len(pattern) - 1:
            leftChar = str1[startIndex]
            startIndex += 1
            if leftChar in charFreq:
                if charFreq[leftChar] == 0:
                    matched -= 1
                charFreq[leftChar] += 1
    
    return anagrams


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()