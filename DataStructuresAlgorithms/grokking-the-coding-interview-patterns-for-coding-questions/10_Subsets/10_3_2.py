# Given a set of distinct numbers, find all of its permutations.
# 
# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
# 1. {1, 2, 3}
# 2. {1, 3, 2}
# 3. {2, 1, 3}
# 4. {2, 3, 1}
# 5. {3, 1, 2}
# 6. {3, 2, 1}
# If a set has ‘n’ distinct elements it will have $n!$ permutations.


def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        # create a new permutation by adding the current number at every position
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            generate_permutations_recursive(
                nums, index+1, newPermutation, result)


def main():
    print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()