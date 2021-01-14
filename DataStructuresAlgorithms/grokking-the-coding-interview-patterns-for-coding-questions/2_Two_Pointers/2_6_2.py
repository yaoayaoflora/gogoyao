# Write a function to return the list of all such triplets instead of the count. How will
# the time complexity change in this case?

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        search_pairs(arr, target-arr[i], i, triplets)
    
    return triplets


def search_pairs(arr, targetSum, i, triplets):
    j = i + 1
    k = len(arr) - 1
    while j < k:
        if arr[j] + arr[k] < targetSum:
            for idx in range(k, j, -1):
                triplets.append([arr[i], arr[j], arr[idx]])
            j += 1
        if arr[j] + arr[k] >= targetSum:
            k -= 1


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()

# [[-1, 0, 3], [-1, 0, 2]]
# [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]