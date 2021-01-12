# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any
# contiguous subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
    startIndex = 0
    maxSum = 0
    currentSum = 0

    for endIndex in range(len(arr)):
        currentSum += arr[endIndex]
        maxSum = max(maxSum, currentSum)

        if endIndex >= k - 1:
            currentSum -= arr[startIndex]
            startIndex += 1
    
    return maxSum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
        