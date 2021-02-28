# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.


from heapq import *


def find_k_largest_numbers(nums, k):
    minHeap = []

    # put first 'K' numbers in the min-heap
    for i in range(k):
        heappush(minHeap, nums[i])

    # go through the remaining numbers of the array, if the number from the array is bigger than the 
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)


def main():

    print("Here are the top K numbers: " +
                str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
                str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()