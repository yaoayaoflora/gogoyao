# Given a string and a pattern, find the smallest substring in the given string which has all the
# characters of the given pattern.

def find_substring(str1, pattern):
    startIndex = 0
    minLength = len(str1) + 1
    resultIndex = 0
    matched = 0
    charFreqToMatch = {}

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
        
        while matched == len(charFreqToMatch):
            if endIndex - startIndex + 1 < minLength:
                minLength = endIndex - startIndex + 1
                resultIndex = startIndex
            
            leftChar = str1[startIndex]
            startIndex += 1
            if leftChar in charFreqToMatch:
                if charFreqToMatch[leftChar] == 0:
                    matched -= 1
                charFreqToMatch[leftChar] += 1
        
    if minLength == len(str1) + 1:
        return ''
    
    return str1[resultIndex:resultIndex+minLength]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))

main()
                


