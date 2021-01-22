# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

import math


def shortest_window_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < len(arr) - 1 and arr[left] <= arr[left+1]:
        left += 1
    
    if left == len(arr) - 1:
        return 0

    while right > 0 and arr[right] >= arr[right-1]:
        right -= 1

    subarrayMin = math.inf
    subarrayMax = -math.inf
    for i in range(left, right+1):
        subarrayMin = min(subarrayMin, arr[i])
        subarrayMax = max(subarrayMax, arr[i])

    while left > 0 and arr[left-1] > subarrayMin:
        left -= 1

    while right < len(arr) - 1 and arr[right+1] < subarrayMax:
        right += 1

    return right - left + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()

# 5 
# 5 
# 0
# 3