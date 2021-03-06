<<<<<<< HEAD
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
=======
from Graph import Graph
from Queue import MyQueue
from Stack import MyStack


def bfs_traversal_helper(g, source, visited):
    result = ""
    # Create Queue(implemented in previous lesson) for Breadth First Traversal
    # and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True # Mark as visited
    # Traverse while queue is not empty
    while(queue.is_empty() is False):
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next_element
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result
    


g = Graph(4)
num_of_vertices = g.vertices

if num_of_vertices == 0:
    print("Graph is empty")
elif num_of_vertices < 0:
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    print(bfs_traversal(g, 0))
>>>>>>> 763a5b4694e96a79e4cb6e3afbacdc33308e76a8
