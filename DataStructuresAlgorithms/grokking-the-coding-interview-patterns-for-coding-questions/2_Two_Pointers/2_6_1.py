# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
# arr[i] + arr[j] + arr[k] < target where i , j , and k are three different indices. Write a
# function to return the count of such triplets.


def search_triplets(arr, target):
    arr.sort()
    count = 0

    for i in range(len(arr)-2):
        count += search_pairs(arr, target, i)
    
    return count


def search_pairs(arr, targetSum, firstIdx):
    left = firstIdx + 1
    right = len(arr) - 1
    count = 0

    while left < right:
        currentSum = arr[firstIdx] + arr[left] + arr[right]
        if currentSum < targetSum:
            count += right - left
            left += 1
        else:
            right -= 1
        
    return count


def main():
    print(search_triplets([-1, 0, 2, 3], 3))
    print(search_triplets([-1, 4, 2, 1, 3], 5))


main()

# 2
# 4