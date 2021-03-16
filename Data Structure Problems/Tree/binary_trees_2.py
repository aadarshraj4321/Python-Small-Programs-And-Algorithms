

class BinaryNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTreeUpdate:
    def printBinaryTree(self, root):
        if(root == None):
            return
        print(root.data, end = ":")
        if(root.left != None):
            print(" R ", root.left.data, end = ",")
        if(root.right != None):
            print(" L ", root.right.data)
        print()
        self.printBinaryTree(root.left)
        self.printBinaryTree(root.right)
        
    def takeInput(self):
        rootData = int(input())
        if(rootData == -1):
            return
        root = BinaryNode(rootData)
        leftTree = self.takeInput()
        rightTree = self.takeInput()
        root.left = leftTree
        root.right = rightTree
        return root

    def numNodes(self, root):
        if(root == None):
            return 0
        left = self.numNodes(root.left)
        right = self.numNodes(root.right)
        return 1 + left + right

    def largestData(self, root):
        if(root == None):
            return -1
        leftLargest = self.largestData(root.left)
        rightLargest = self.largestData(root.right)
        largest = max(leftLargest, rightLargest, root.data)
        return largest

    def heightofTree(self, root):
        if(root == None):
            return 0
        leftHeight = self.heightofTree(root.left)
        rightHeight = self.heightofTree(root.right)
        largestHeight = max(leftHeight,rightHeight)
        return largestHeight + 1

    def numofLeafNodes(self, root):
        if(root == None):
            return 0
        if(root.left == None and root.right == None):
            return 1
        leftLeaf = self.numofLeafNodes(root.left)
        rightLeaf = self.numofLeafNodes(root.right)
        return leftLeaf + rightLeaf

    def printDepthK(self, root, k):
        if(root == None):
            return
        if(k == 0):
            print(root.data)
            return
        self.printDepthK(root.left, k - 1)
        self.printDepthK(root.right, k - 1)

    def printDepthKV2(self, root, k, d = 0):
        if(root == None):
            return

        if(k == d):
            print(root.data)
        self.printDepthKV2(root.left, k, d + 1)
        self.printDepthKV2(root.right, k, d + 1)
        




bt = BinaryTreeUpdate()
root = bt.takeInput()
bt.printBinaryTree(root)
print()
print(bt.numNodes(root))
print(bt.largestData(root))
print(bt.heightofTree(root))
print(bt.numofLeafNodes(root))
bt.printDepthK(root, 2)
bt.printDepthKV2(root, 2)






    

