

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinaryTree:
    def isBalanced(self, root):
        pass

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
            return None
        print(root.data, end = ":")
        if(root.left != None):
            print(" L ", root.left.data, end = " , ")
        if(root.right != None):
            print(" R ", root.right.data)
        print()
        self.printTree(root.left)
        self.printTree(root.right)


bt = BinaryTree()
root = bt.takeInput()
bt.printTree(root)
