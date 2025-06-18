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
    def insert_start(self , data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp
        temp.prev = new_node
    def insert_middle(self , data , position):
        new_node = Node(data)
        pointer = self.head
        current = 1
        while current < position - 1:
            pointer = pointer.next
            current = current +1 
        temp = pointer.next
        pointer.next = new_node
        new_node.next = temp
        new_node.prev = pointer
        temp.prev = new_node
    def delete_end(self):
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer = pointer.prev
        pointer.next = None
    def delete_start(self):
        pointer = self.head
        self.head = pointer.next
        self.head.prev = None
    def delete_middle(self , position):
        pointer = self.head
        current = 1
        while current < position:
            pointer = pointer.next
            current = current + 1
            previous_pointer = pointer.prev
            next_pointer = pointer.next
            previous_pointer.next = next_pointer
            next_pointer.prev = previous_pointer
    def traversal(self):
        pointer = self.head
        while pointer:
            print(pointer.data , end = "< - >")
            pointer = pointer.next
        print()
dll = double_linked_list()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.traversal()
dll.insert_start(50)
dll.traversal()
dll.insert_middle(60 , 3)
dll.traversal()
dll.delete_middle(3)
dll.traversal()