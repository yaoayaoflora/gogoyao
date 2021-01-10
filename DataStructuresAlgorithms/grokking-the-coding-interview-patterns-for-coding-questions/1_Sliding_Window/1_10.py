# Given a string and a pattern, find the smallest substring in the given string which has all the
# characters of the given pattern.

def find_substring(str1, pattern):
    startIndex = 0
    matched = 0
    minLength = len(str1) + 1
    toMatch = {}
    subString = ''

    for char in pattern:
        if char not in toMatch:
            toMatch[char] = 0
        toMatch[char] += 1

    for endIndex in range(len(str1)):
        rightChar = str1[endIndex]
        if rightChar in toMatch:
            toMatch[rightChar] -= 1
            if toMatch[rightChar] == 0:
                matched += 1
        
        while matched == len(toMatch):
            leftChar = str1[startIndex]
            if minLength > endIndex - startIndex + 1:
                minLength = endIndex - startIndex + 1
                subString = str1[startIndex:endIndex+1]
            startIndex += 1
            if leftChar in toMatch:
                if toMatch[leftChar] == 0:
                    matched -= 1
                toMatch[leftChar] += 1
                    
    return subString


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))

main()
                


