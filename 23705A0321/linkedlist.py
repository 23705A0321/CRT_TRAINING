class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display_with_addresses(self):
        current = self.head
        while current:
            print(f"[Data: {current.data} | Node Addr: {hex(id(current))} | Next Addr: {hex(id(current.next)) if current.next else None}]")
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display_with_addresses()
