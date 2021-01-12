# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray 
# whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

def smallest_subarray_with_given_sum(s, arr):
    startIndex = 0
    currenSum = 0
    minLength = len(arr) + 1

    for endIndex in range(len(arr)):
        currenSum += arr[endIndex]

        while currenSum >= s:
            minLength = min(minLength, endIndex - startIndex + 1)
            currenSum -= arr[startIndex]
            startIndex += 1
        
    if minLength == len(arr) + 1:
        return 0
    
    return minLength


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()