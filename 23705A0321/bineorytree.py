class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertion(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        return
                    current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right
                else:
                    return 

    def preorder(self):
        def pre_order(node, result):
            if node:
                result.append(node.data)
                pre_order(node.left, result)
                pre_order(node.right, result)
        result = []
        pre_order(self.root, result)
        return result

    def postorder(self):
        def post_order(node, result):
            if node:
                post_order(node.left, result)
                post_order(node.right, result)
                result.append(node.data)
        result = []
        post_order(self.root, result)
        return result

    def inorder(self):
        def in_order(node, result):
            if node:
                in_order(node.left, result)
                result.append(node.data)
                in_order(node.right, result)
        result = []
        in_order(self.root, result)
        return result


data = [40, 10, 2, 108, 50, 22, 77, 1, 3, 84, 63]
bts = BinaryTree()
for value in data:
    bts.insertion(value)

print("Preorder : ", bts.preorder())
print("Postorder : ", bts.postorder())
print("Inorder : ", bts.inorder())