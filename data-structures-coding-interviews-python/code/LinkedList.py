from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False
        
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next_element = self.get_head()
        self.head_node = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
            return None
        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = new_node
        return None
    
    def length(self):
        if self.is_empty():
            return 0
        len = 0
        current_node = self.get_head()
        while current_node:
            len += 1
            current_node = current_node.next_element
        return len

    def search(self, value):
        current_node = self.get_head()
        while current_node is not None:
            if current_node.data == value:
                return True
            current_node = current_node.next_element
        return False
    
    def delete_at_head(self):
        first_element = self.get_head()
        if first_element:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return None
    
    def delete(self, value):
        if self.is_empty():
            return 'The list is empty!'
        
        previous_node = None
        current_node = self.get_head()

        if current_node.data == value:
            self.delete_at_head()
            return '{} was deleted!'.format(value)
        
        while current_node:
            if current_node.data == value:
                last_element.next_element = current_node.next_element
                current_node.next_element = None
                return '{} was deleted!'.format(value)
            last_element = current_node
            current_node = current_node.next_element
        return '{} is not in the list!'.format(value)


    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True