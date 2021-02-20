# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from
# position ‘p’ to ‘q’.


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head
    
    i = 0
    previous, current = None, head
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    last_part_tail = previous
    sub_list_tail = current
    next = None
    i = 0
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    if last_part_tail is not None:
        last_part_tail.next = previous
    else:
        head = previous

    sub_list_tail.next = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()