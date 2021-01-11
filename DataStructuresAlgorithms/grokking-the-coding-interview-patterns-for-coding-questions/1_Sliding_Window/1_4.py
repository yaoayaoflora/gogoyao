# Given an array of characters where each character represents a fruit tree, you are given two 
# baskets and your goal is to put maximum number of fruits in each basket. The only 
# restriction is that each basket can have only one type of fruit.
# 
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one
# fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# 
# Write a function to return the maximum number of fruits in both the baskets.

def fruits_into_baskets(fruits):
    startIndex = 0
    maxLength = 0
    countFruits = {}

    for endIndex in range(len(fruits)):
        rightFruit = fruits[endIndex]
        if rightFruit not in countFruits:
            countFruits[rightFruit] = 0
        countFruits[rightFruit] += 1

        while len(countFruits) > 2:
            leftFruit = fruits[startIndex]
            startIndex += 1
            countFruits[leftFruit] -= 1
            if countFruits[leftFruit] == 0:
                del countFruits[leftFruit]
        
        maxLength = max(maxLength, endIndex - startIndex + 1)

    return maxLength


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()