
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def takeInput(self):
        data = int(input())
        if(data == -1):
            return
        root = Node(data)
        left = self.takeInput()
        right = self.takeInput()
        root.left = left
        root.right = right
        return root

    def printTree(self, root):
        if(root == None):
            return
        print(root.data, end=":")
        if(root.left != None):
            print(" L ", root.left.data, end=",")
        if(root.right != None):
            print(" R ", root.right.data)
        print()
        self.printTree(root.left)
        self.printTree(root.right)

    def treeHeight(self, root):
        if(root == None):
            return 0
        left = self.treeHeight(root.left)
        right = self.treeHeight(root.right)
        longestHeight = max(left, right)
        return longestHeight + 1



bt = BinaryTree()
root = bt.takeInput()
bt.printTree(root)
print()
print()
print(bt.treeHeight(root))
