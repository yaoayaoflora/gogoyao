# Given a set of numbers that might contain duplicates, find all of its distinct subsets.


def find_subsets(nums):
    # sort the numbers to handle duplicates
    nums.sort()
    subsets = []
    subsets.append([])

    for i in range(len(nums)):
        startIndex = 0
        # if the current and the previous number are the same, create new subsets only from the subsets
        # added in the previous step
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1

        for j in range(startIndex, endIndex+1):
            # create a new subset from the existing subset and add the current element to it
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()