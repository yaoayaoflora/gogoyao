# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing
# positive numbers in the array.


def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers) < k:
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                extraNumbers.add(nums[i])
    
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = n + i
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
        i += 1
    
    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()

# [1, 2, 6]
# [1, 5, 6]
# [1, 2]