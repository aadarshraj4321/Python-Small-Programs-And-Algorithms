

class Binary:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryUpdates:
    def takeInput(self):
        rawData = int(input())
        if(rawData == -1):
            return
        root = Binary(rawData)
        left = self.takeInput()
        right = self.takeInput()
        root.left = left
        root.right = right
        return root

    def largestBinary(self, root):
        if(root == None):
            return -1
        leftLargest = self.largestBinary(root.left)
        rightLargest = self.largestBinary(root.right)
        largest = max(leftLargest, rightLargest, root.data)
        return largest
    
    def printBinary(self, root):
        if(root == None):
            return
        print(["", root.data, ""], end=",")
        if(root.left != None):
            print([root.left.data, "", ""])
        if(root.right != None):
            print(["", "", root.right.data])
        print()
        self.printBinary(root.left)
        self.printBinary(root.right)

    def leafNode(self, root):
        if(root == None):
            return 0
        leftHeight = self.leafNode(root.left)
        rightHeight = self.leafNode(root.right)
        largestHeight = max(leftHeight, rightHeight)
        return largestHeight + 1
        

bt = BinaryUpdates()
root = bt.takeInput()
#bt.printBinary(root)
print(bt.leafNode(root))
print(bt.largestBinary(root))
