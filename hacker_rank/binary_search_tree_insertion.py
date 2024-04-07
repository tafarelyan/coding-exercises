class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if current.info > val: 
                if not current.left:
                    current.left = Node(val)
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(val)
                    break
                else:
                    current = current.right
            

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)
    preOrder(tree.root)