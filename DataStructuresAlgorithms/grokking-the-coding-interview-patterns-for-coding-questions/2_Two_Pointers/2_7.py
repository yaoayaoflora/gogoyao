# Given an array with positive numbers and a target number, find all of its contiguous subarrays
# whose product is less than the target number.

from collections import deque


def find_subarrays(arr, target):
    startIndex = 0
    product = 1
    result = []

    for endIndex in range(len(arr)):
        product *= arr[endIndex]
        while product >= target and startIndex < len(arr):
            product /= arr[startIndex]
            startIndex += 1

        temp_list = deque()
        for i in range(endIndex, startIndex-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
        
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()

# [[2], [5], [2, 5], [3], [5, 3], [10]]
# [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
