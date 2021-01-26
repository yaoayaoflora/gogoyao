# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
# Your algorithm should use constant space and the input LinkedList should be in the original form 
# once the algorithm is finished. 
# 
# The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    if head is None and head_second_half is None:
        return True

    return False


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

# Is palindrome: True
# Is palindrome: False