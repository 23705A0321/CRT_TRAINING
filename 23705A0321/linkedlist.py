class Node:
    def __init__(self , data):
        self.data = data
        self.prev = None
        self.next = None
class double_linked_list:
    def __init__(self):
        self.head = None
    def insert_end(self , data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
            new_node.prev = pointer
    def insert_start
    
    
    
dll = double_linked_list()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.traversal()
dll.insert_start(50)
