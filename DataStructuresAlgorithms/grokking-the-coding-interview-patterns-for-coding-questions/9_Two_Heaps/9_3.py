# Given a set of investment projects with their respective profits, we need to find the most profitable projects. 
# We are given an initial capital and are allowed to invest only in a fixed number of projects. 
# Our goal is to choose projects that give us the maximum profit.
# 
# We can start an investment project only when we have the required capital. Once a project is selected, 
# we can assume that its profit has become our capital.


from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    # insert all project capitals to a min-heap
    for i in range(len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    # let's try to find a total of 'numberOfProjects' best projects
    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        # find all projects that can be selected within the available capital and insert them in a max-heap
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        # terminate if we are not able to find any project that can be completed within the available capital
        if not maxProfitHeap:
            break

        # select the project with the maximum profit
        availableCapital += -heappop(maxProfitHeap)[0]

    return availableCapital


def main():
    print("Maximum capital: " +
                str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
                str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()