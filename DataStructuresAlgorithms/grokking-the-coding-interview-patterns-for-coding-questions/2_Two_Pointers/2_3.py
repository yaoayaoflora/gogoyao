# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

def make_squares(arr):
    left = 0
    right = len(arr) - 1
    highestSquareIdx = len(arr) - 1
    squares = [0 for i in range(len(arr))]

    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

        if leftSquare <= rightSquare:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        else:
            squares[highestSquareIdx] = leftSquare
            left += 1
        highestSquareIdx -= 1

    return squares
    

def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

# Squares: [0, 1, 4, 4, 9]
# Squares: [0, 1, 1, 4, 9]