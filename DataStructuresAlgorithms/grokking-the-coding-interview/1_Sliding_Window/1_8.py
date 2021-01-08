# Given a string and a pattern, find out if the string contains any permutation of the pattern.
def find_permutation(str1, pattern):
    startIndex = 0
    matched = 0
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
            return True
        
        if endIndex >= len(pattern) - 1:
            leftChar = str1[startIndex]
            startIndex += 1
            if leftChar in charFreq:
                if charFreq[leftChar] == 0:
                    matched -= 1
                charFreq[leftChar] += 1
    
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()