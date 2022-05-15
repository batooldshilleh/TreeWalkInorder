class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):
    if root:

        printInorder(root.left)

        print(root.val),

        printInorder(root.right)



# Driver code
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

printInorder(root)

