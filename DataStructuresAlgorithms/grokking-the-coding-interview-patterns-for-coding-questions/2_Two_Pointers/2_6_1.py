# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
# arr[i] + arr[j] + arr[k] < target where i , j , and k are three different indices. Write a
# function to return the count of such triplets.

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += search_pairs(arr, target-arr[i], i)
    
    return count


def search_pairs(arr, targetSum, i):
    j = i + 1
    k = len(arr) - 1
    count = 0
    while j < k:
        if arr[j] + arr[k] < targetSum:
            count += k - j
            j += 1
        if arr[j] + arr[k] >= targetSum:
            k -= 1
    
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()

# 2
# 4