# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.


def search_triplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pairs(arr, -arr[i], i, triplets)

    return triplets


def search_pairs(arr, targetSum, firstIdx, triplets):
    left = firstIdx + 1
    right = len(arr) - 1

    while left < right:
        curretnSum = arr[left] + arr[right]
        if curretnSum == targetSum:
            triplets.append([-targetSum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif curretnSum < targetSum:
            left += 1
        else:
            right -= 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()

# [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# [[-5, 2, 3], [-2, -1, 3]]