class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insertion(self , data):
        new_node = Node(data)
        print(new_node.data , new_node.left , new_node.right)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left == None:
                        current.left = new_node
                        return
                    current = current.left
                if data > current.data:
                    if current.right == None:
                        current.right = new_node
                        return
                    current = current.right
                        
            

data = [40 , 10 , 2 , 108 , 50 , 22 , 77 , 1 , 3 , 84 , 63]
bts = BinaryTree()
for value in data:
    bts.insertion(value)

        
        
        