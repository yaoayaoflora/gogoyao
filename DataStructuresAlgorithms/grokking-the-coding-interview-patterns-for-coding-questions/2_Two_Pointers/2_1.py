# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is
# equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to
# the given target.


def pair_with_targetsum(arr, targetSum):
    left = 0
    right = len(arr) - 1

    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return [left, right]
        if currentSum > targetSum:
            right -= 1
        if currentSum < targetSum:
            left += 1
    
    return [-1, -1]
    

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

# [1, 3]
# [0, 2]