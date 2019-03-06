class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    
    def __init__(self):
        self.root = None

    def preorderTraversal_sub(self, n:Node):
        if (n != None):
            print(n.data)
            self.preorderTraversal_sub(n.left)
            self.preorderTraversal_sub(n.right)

    def preorderTraversal(self):
        self.preorderTraversal_sub(self.root)
        
    def addNumber(self, num):
        self.addNumber_helper(self.root, num)

    def addNumber_helper(self, node, num):
        if node == None:
            self.root = Node(num)
        else:
            if node.data > num:
                if node.left is None:
                    node.left = Node(num)
                else:
                    self.addNumber_helper(node.left, num)
            else:
                if node.right is None:
                    node.right = Node(num)
                else:
                    self.addNumber_helper(node.right, num)

