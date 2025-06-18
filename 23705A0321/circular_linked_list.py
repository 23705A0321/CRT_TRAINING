class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class circular_linked_list:
    def __init__(self):
        self.head = None
    def insert_end(self , data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            pointer.next = new_node
            new_node.next = self.head
    def insert_start(self , data):
        new_node = Node(data)
        pointer = self.head
        while pointer.next != self.head:
            pointer = pointer.next
        pointer.next = new_node
        temp = self.head
        new_node.next = temp
        self.head = new_node
    def delete_last(self):
        pointer = self.head
        while pointer.next != self.head:
            temp = pointer
            pointer = pointer.next
        temp.next = self.head

    def traversal(self):
        pointer = self.head
        while pointer.next != self.head:
            print(pointer.data , end = "< - >")
            pointer = pointer.next
        print(pointer.data)
            
cll = circular_linked_list()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_end(40)
cll.insert_end(50)
cll.insert_end(60)
cll.insert_end(70)
cll.traversal()
cll.insert_start(100)
cll.traversal()
cll.delete_last()
cll.traversal()