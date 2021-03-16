

class BinaryTree:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


class BinaryTreeUpdates:
    def printBinaryTree(self, root):
        if(root == None):
            return
        print(root.data, end=" : ")
        if(root.left != None):
            print("L", root.left.data, end = " , ")
        if(root.right != None):
            print("R", root.right.data, end = " , ")
        print()
        self.printBinaryTree(root.left)
        self.printBinaryTree(root.right)


b1 = BinaryTree(100)
b2 = BinaryTree(50)
b3 = BinaryTree(200)

b4 = BinaryTree(150)
b5 = BinaryTree(250)

b6 = BinaryTree(40)
b7 = BinaryTree(80)

b1.left = b2
b1.right = b3

b2.left = b6
b2.right = b7

b3.left = b4
b3.right = b5


b = BinaryTreeUpdates()
b.printBinaryTree(b1)
