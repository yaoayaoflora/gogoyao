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

    subarrayMax = -math.inf
    subarrayMin = math.inf
    for i in range(left, right+1):
        subarrayMax = max(subarrayMax, arr[i])
        subarrayMin = max(subarrayMin, arr[i])

    while left > 0 and arr[left-1] > subarrayMin:
        left -= 1
    
    while right < len(arr) - 1 and arr[right+1] <subarrayMax:
        right += 1
    
    return right - left + 1
    














def shortest_window_sort(arr):
    low = 0
    high = len(arr) - 1
    
    # find the first number out of sorting order from the beginning
    while low < len(arr) - 1 and arr[low] <= arr[low+1]:
        low += 1
    if low == len(arr) - 1:
        return 0

    # find the first number out of sorting order from the end
    while high > 0 and arr[high] >= arr[high-1]:
        high -= 1

    # find the maximum and minimum of the subarry
    subarrayMax = -math.inf
    subarrayMin = math.inf
    for k in range(low, high+1):
        subarrayMax = max(subarrayMax, arr[k])
        subarrayMin = min(subarrayMin, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low-1] > subarrayMin:
        low -= 1

    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < len(arr) - 1 and arr[high+1] < subarrayMax:
        high += 1
    
    return high - low + 1


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