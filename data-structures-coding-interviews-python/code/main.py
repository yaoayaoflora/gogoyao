from LinkedList import LinkedList
from Node import Node

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
print(lst.delete(2))
lst.print_list()