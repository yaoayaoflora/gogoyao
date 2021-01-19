# Given an array of unsorted numbers and a target number, find a triplet in the array whose
# sum is as close to the target number as possible, return the sum of the triplet. If there are
# more than one such triplet, return the sum of the triplet with the smallest sum.

import math

def triplet_sum_close_to_target(arr, targetSum):
    arr.sort()
    minAbsDiff = math.inf
    resultSum = 0

    for i in range(len(arr)-2):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            currentSum = arr[i] + arr[j] + arr[k]
            if currentSum == targetSum:
                return currentSum
            elif currentSum < targetSum:
                j += 1
            else:
                k -= 1
            
            currentDiff = currentSum - targetSum
            if abs(currentDiff) <= minAbsDiff:
                minAbsDiff = abs(currentDiff)
                if currentDiff < 0:
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