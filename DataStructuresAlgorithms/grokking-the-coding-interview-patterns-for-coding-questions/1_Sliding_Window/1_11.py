# Given a string and a list of words, find all the starting indices of substrings in the given string 
# that are a concatenation of all the given words exactly once without any overlapping of words. 
# It is given that all words are of the same length.

def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    wordsFrequency = {}
    for word in words:
        if word not in wordsFrequency:
            wordsFrequency[word] = 0
        wordsFrequency[word] += 1
    
    wordsCount = len(words)
    wordsLength = len(words[0])
    resultIndices = []

    for i in range(len(str1) + 1 - wordsCount * wordsLength):
        wordsSeen = {}
        for j in range(wordsCount):
            nextWordIndex = i + j * wordsLength
            word = str1[nextWordIndex:nextWordIndex+wordsLength]
            
            if word not in wordsFrequency:
                break

            if word not in wordsSeen:
                wordsSeen[word] = 0
            wordsSeen[word] += 1

            if wordsSeen[word] > wordsFrequency[word]:
                break

            if j + 1 == wordsCount:
                resultIndices.append(i)
    
    return resultIndices




def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()