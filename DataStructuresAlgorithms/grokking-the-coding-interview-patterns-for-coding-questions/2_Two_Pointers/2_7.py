# Given an array with positive numbers and a target number, find all of its contiguous subarrays
# whose product is less than the target number.

from collections import deque


def find_subarrays(arr, target):
    left = 0
    product = 1
    subarrays = []

    for right in range(len(arr)):
        product *= arr[right]
        
        while product >= target:
            product /= arr[left]
            left += 1
        
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            subarrays.append(list(temp_list))
        
    return subarrays
    

def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()

# [[2], [5], [2, 5], [3], [5, 3], [10]]
# [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
