# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray 
# whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
import math

def smallest_subarray_with_given_sum(s, arr):
    windowStart = 0
    minLength = math.inf
    windowSum = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if minLength == math.inf:
        return 0
    
    return minLength


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()