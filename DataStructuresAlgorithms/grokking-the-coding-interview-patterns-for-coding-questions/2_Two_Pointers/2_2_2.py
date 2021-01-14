# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’
# in-place and return the new length of the array.

def remove_element(arr, key):
    nextElement = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    
    return nextElement


def main():
    print("Array new length: " + str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " + str(remove_element([2, 11, 2, 2, 1], 2)))


main()