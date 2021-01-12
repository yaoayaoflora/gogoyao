# Given a string and a pattern, find out if the string contains any permutation of the pattern.

def find_permutation(str1, pattern):
    startIndex = 0
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
        
        if matched == len(charFreqToMatch):
            return True
        
        if endIndex >= len(pattern) - 1:
            leftChar = str1[startIndex]
            startIndex += 1
            if leftChar in charFreqToMatch:
                if charFreqToMatch[leftChar] == 0:
                    matched -= 1
                charFreqToMatch[leftChar] += 1
        
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()