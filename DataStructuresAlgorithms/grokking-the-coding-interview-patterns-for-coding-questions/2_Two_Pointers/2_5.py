# Given an array of unsorted numbers and a target number, find a triplet in the array whose
# sum is as close to the target number as possible, return the sum of the triplet. If there are
# more than one such triplet, return the sum of the triplet with the smallest sum.

import math

def triplet_sum_close_to_target(arr, targetSum):
    arr.sort()
    resultSum = 0
    minAbsDiff = math.inf
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == targetSum:
                return targetSum
            if currentSum < targetSum:
                left += 1
            if currentSum > targetSum:
                right -= 1
            
            currentDiff = targetSum - currentSum
            if abs(currentDiff) <= minAbsDiff:
                minAbsDiff = abs(currentDiff)
                if currentDiff > 0:
                    resultSum = currentSum
    
    return resultSum

        
def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()

# 1
# 0
# 3