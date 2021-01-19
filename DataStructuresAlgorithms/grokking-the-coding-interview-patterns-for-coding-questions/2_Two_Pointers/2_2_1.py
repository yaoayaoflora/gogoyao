# Given an array of sorted numbers, remove all duplicates from it. You should not use any
# extra space; after removing the duplicates in-place return the new length of the array.

def remove_duplicates(arr):
    nextNonDuplicateIdx = 1
    i = 0
    while i <= len(arr) - 1:
        if i > 0 and arr[i] != arr[i-1]:
            arr[nextNonDuplicateIdx] = arr[i]
            nextNonDuplicateIdx += 1
        i += 1

    return nextNonDuplicateIdx



def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()

# 4
# 2