# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of 
# the square of all of its digits, leads us to number ‘1’. All other (not- happy) numbers will never reach ‘1’. 
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.


def find_happy_number(num):
    fast, slow = num, num

    while True:
        fast = find_square_sum(find_square_sum(fast))
        slow = find_square_sum(slow)
        if fast == slow:
            break

    return fast == 1


def find_square_sum(num):
    square_sum = 0

    while num > 0:
        digit = num % 10
        square_sum += digit * digit
        num //= 10

    return square_sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

# True
# False