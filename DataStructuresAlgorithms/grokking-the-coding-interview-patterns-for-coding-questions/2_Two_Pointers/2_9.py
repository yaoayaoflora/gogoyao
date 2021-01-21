# Given an array of unsorted numbers and a target number, find all unique quadruplets in it,
# whose sum is equal to the target number.


def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []

    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
        
    return quadruplets


def search_pairs(arr, targetSum, firstIdx, SecondIdx, quadruplets):
    left = SecondIdx + 1
    right = len(arr) - 1

    while left < right:
        currentSum = arr[firstIdx] + arr[SecondIdx] + arr[left] + arr[right]
        if currentSum == targetSum:
            quadruplets.append([arr[firstIdx], arr[SecondIdx], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()

# [[-3, -1, 1, 4], [-3, 1, 1, 2]]
# [[-2, 0, 2, 2], [-1, 0, 1, 2]]