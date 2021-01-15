# Write a function to return the list of all such triplets instead of the count. How will
# the time complexity change in this case?

def search_triplets(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        search_pairs(arr, target, i, triplets)

    return triplets


def search_pairs(arr, targetSum, first, triplets):
    left = first + 1
    right = len(arr) - 1

    while left < right:
        currentSum = arr[first] + arr[left] + arr[right]
        if currentSum < targetSum:
            for j in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[j]])
            left += 1
        else:
            right -= 1


def main():
    print(search_triplets([-1, 0, 2, 3], 3))
    print(search_triplets([-1, 4, 2, 1, 3], 5))


main()

# [[-1, 0, 3], [-1, 0, 2]]
# [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]