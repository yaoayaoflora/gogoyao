# Given a string and a list of words, find all the starting indices of substrings in the given string 
# that are a concatenation of all the given words exactly once without any overlapping of words. 
# It is given that all words are of the same length.

def find_word_concatenation(str1, words):
    wordFreqToMatch = {}
    resultIndices = []
    
    wordLength = len(words[0])
    wordCount = len(words)
    for word in words:
        if word not in wordFreqToMatch:
            wordFreqToMatch[word] = 0
        wordFreqToMatch[word] += 1
    
    for i in range(len(str1) - wordCount * wordLength + 1):
        wordFreqMatched ={}
        for j in range(wordCount):
            startIndex = i + j * wordLength
            nextWord = str1[startIndex:startIndex+wordLength]
            if nextWord not in wordFreqToMatch:
                break
            
            if nextWord not in wordFreqMatched:
                wordFreqMatched[nextWord] = 0
            wordFreqMatched[nextWord] += 1
            if wordFreqMatched[nextWord] > wordFreqToMatch[nextWord]:
                break

            if j + 1 == wordCount:
                resultIndices.append(i)

    return resultIndices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()