# Given a set with distinct elements, find all of its distinct subsets.


def find_subsets(nums):
    subsets = []
    # start by adding the empty subsets
    subsets.append([])
    for currentNumber in nums:
        # take all existing subsets and insert the current number into them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current number into it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()