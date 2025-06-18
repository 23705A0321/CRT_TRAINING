class Stack:
    def __init__(self):
        self.stack = []
    def insert_in_stack(self , data):
        self.stack.append(data)
    def pop_from_stack(self):
        if self.is_empty() == False:
            print("removed from stack : " ,self.stack.pop())
        else:
            print("no data to remove")
    def peek_from_stack(self):
        if self.is_empty() == False:
            print(self.stack[-1])
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
obj = Stack()
obj.insert_in_stack(10)
obj.insert_in_stack(20)
obj.insert_in_stack(30)
obj.insert_in_stack(40)
obj.pop_from_stack()
obj.pop_from_stack()
obj.peek_from_stack()
obj.pop_from_stack()
obj.pop_from_stack()
obj.pop_from_stack()