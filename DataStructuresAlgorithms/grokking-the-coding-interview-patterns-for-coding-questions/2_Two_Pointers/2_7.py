# Given an array with positive numbers and a target number, find all of its contiguous subarrays
# whose product is less than the target number.

from collections import deque


def find_subarrays(arr, target):
    startIdx = 0
    product = 1
    subarrays = []

    for endIdx in range(len(arr)):
        product *= arr[endIdx]
        while startIdx <= endIdx and product >= target:
            product /= arr[startIdx]
            startIdx += 1
        
        temp_list = deque()
        for i in range(endIdx, startIdx-1, -1):
            temp_list.appendleft(arr[i])
            subarrays.append(list(temp_list))

    return subarrays


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()

# [[2], [5], [2, 5], [3], [5, 3], [10]]
# [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
