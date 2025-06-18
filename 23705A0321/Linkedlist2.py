class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertion_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertion_middle(self, data, position):
        new_node = Node(data)
        if position == 1:
            # Insert at start
            new_node.next = self.head
            self.head = new_node
            return
        current = 1
        pointer = self.head
        while current < position - 1 and pointer is not None:
            pointer = pointer.next
            current += 1
        if pointer is None:
            print("Position out of range")
            return
        new_node.next = pointer.next
        pointer.next = new_node

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        pointer = self.head
        while pointer.next.next:
            pointer = pointer.next
        pointer.next = None

    def delete_start(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_middle(self, position):
        if self.head is None:
            return
        if position == 1:
            self.head = self.head.next
            return
        current = 1
        pointer = self.head
        while current < position - 1 and pointer.next is not None:
            pointer = pointer.next
            current += 1
        if pointer.next is None:
            print("Position out of range")
            return
        pointer.next = pointer.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Testing the fixed LinkedList
obj = LinkedList()
obj.insertion(10)
obj.insertion(20)
obj.insertion(30)
obj.insertion(40)
obj.display()          # Output: 10 20 30 40

obj.insertion_start(700)
obj.display()          # Output: 700 10 20 30 40

obj.insertion_middle(80, 3)
obj.display()          # Output: 700 10 80 20 30 40

obj.delete_start()
obj.display()          # Output: 10 80 20 30 40

obj.insertion_middle(3, 2)
obj.display()          # Output: 10 3 80 20 30 40
