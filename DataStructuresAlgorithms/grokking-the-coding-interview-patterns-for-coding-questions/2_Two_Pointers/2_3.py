# Given a sorted array, create a new array containing squares of all the number of the input
# array in the sorted order.

def make_squares(arr):
    squares = []
    nextElement = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

        if leftSquare < rightSquare:
            squares.append(leftSquare)
            left += 1
        elif leftSquare > rightSquare:
            squares.append(rightSquare)
            right -= 1
        else:
            squares.append(leftSquare)
            left += 1
            squares.append(rightSquare)
            right -= 1
        




def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
        
