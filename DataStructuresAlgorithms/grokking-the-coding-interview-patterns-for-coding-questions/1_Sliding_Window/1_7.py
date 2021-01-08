# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

def length_of_longest_substring(arr, k):
    startIndex = 0
    maxLength = 0
    maxOnesCount = 0

    for endIndex in range(len(arr)):
        if arr[endIndex] == 1:
            maxOnesCount += 1
        while endIndex - startIndex + 1 - maxOnesCount > k:
            if arr[startIndex] == 1:
                maxOnesCount -= 1
            startIndex += 1
        maxLength = max(maxLength, endIndex - startIndex + 1)
    
    return maxLength


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
        