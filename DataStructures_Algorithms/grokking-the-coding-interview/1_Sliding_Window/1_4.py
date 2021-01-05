# Given an array of characters where each character represents a fruit tree, you are given two 
# baskets and your goal is to put maximum number of fruits in each basket. The only 
# restriction is that each basket can have only one type of fruit.
# 
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one
# fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# 
# Write a function to return the maximum number of fruits in both the baskets.

def fruits_into_baskets(fruits):
    start = 0
    maxLength = 0
    fruitFreq = {}

    for end in range(len(fruits)):
        rightFruit = fruits[end]
        if rightFruit not in fruitFreq.keys():
            fruitFreq[rightFruit] = 0
        fruitFreq[rightFruit] += 1
        while len(fruitFreq) > 2:
            leftFruit = fruits[start]
            fruitFreq[leftFruit] -= 1
            if fruitFreq[leftFruit] == 0:
                del fruitFreq[leftFruit]
            start += 1
        maxLength = max(maxLength, end - start + 1)
    return maxLength


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()