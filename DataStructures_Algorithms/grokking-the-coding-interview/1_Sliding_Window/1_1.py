# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any
# contiguous subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
    windowStart = 0
    maxSum = 0
    windowSum = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd - windowStart >= k: # windowEnd >= k - 1
            windowSum -= arr[windowStart]
            windowStart += 1
        maxSum = max(maxSum, windowSum)
    
    return maxSum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
        