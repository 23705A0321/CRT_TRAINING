class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class double_linked_list:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = new_node
            new_node.prev = pointer

    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_start(self):
        if self.head is None:
            print("List is empty, nothing to delete at start.")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete at end.")
            return
        if self.head.next is None:
            self.head = None
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.prev.next = None

    def delete_middle(self, data):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        pointer = self.head
        # If head node is the node to delete
        if pointer.data == data:
            self.delete_start()
            return
        
        # Search for the node with data
        while pointer is not None and pointer.data != data:
            pointer = pointer.next
        
        # If node not found
        if pointer is None:
            print(f"Node with data {data} not found.")
            return
        
        # If node is last node
        if pointer.next is None:
            self.delete_end()
            return
        
        # Node is somewhere in the middle
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev

    def traversal(self):
        if self.head is None:
            print("List is empty.")
            return
        pointer = self.head
        while pointer is not None:
            print(pointer.data, end=" <-> " if pointer.next else "")
            pointer = pointer.next
        print()

# Example usage:

dll = double_linked_list()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.insert_end(50)
dll.traversal()  # 10 <-> 20 <-> 30 <-> 40 <-> 50

dll.delete_middle(30)
dll.traversal()  # 10 <-> 20 <-> 40 <-> 50

dll.delete_middle(10)
dll.traversal()  # 20 <-> 40 <-> 50

dll.delete_middle(50)
dll.traversal()  # 20 <-> 40

dll.delete_middle(100)  # Node with data 100 not found.
