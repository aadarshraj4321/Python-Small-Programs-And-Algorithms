
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

    def treePrint(self, root):
        left = []
        right = []
        if(root == None):
            return
        left.append(root.data)
        right.append(root.data)
        if(root.left != None):
            left.append(root.left.data)
        if(root.right != None):
            right.append(root.right.data)
        self.treePrint(root.left)
        self.treePrint(root.right)
        return left, right

    def removeLeaf(self, root):
        if(root == None):
            return None
        if(root.left == None and root.right == None):
            return None
        root.left = self.removeLeaf(root.left)
        root.right = self.removeLeaf(root.right)
        return root

    def height(self, root):
        if(root == None):
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if(root == None):
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if(left - right > 1 or right - left > 1):
            return False
        isLeftBalanced = self.isBalanced(root.left)
        isRightBalanced = self.isBalanced(root.right)
        if(isLeftBalanced and isRightBalanced):
            return True
        else:
            return False

tree = BinaryTree()
root = tree.takeInput()
tree.printTree(root)
#print(tree.treePrint(root))
#print()
#root = tree.removeLeaf(root)
#tree.printTree(root)
print(tree.isBalanced(root))
