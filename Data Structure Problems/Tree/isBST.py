import queue

class Binary:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryDetails:
    def takeInput(self):
        q = queue.Queue()
        rootData = int(input())
        if(rootData == -1):
            return None
        root = Binary(rootData)
        q.put(root)
        while(not(q.empty())):
            currentNode = q.get()
            print("Enter left child of ", currentNode.data)
            leftChildData = int(input())
            if(leftChildData != -1):
                leftChild = Binary(leftChildData)
                currentNode.left = leftChild
                q.put(leftChild)
            print("Enter right child of ", currentNode.data)
            rightChildData = int(input())
            if(rightChildData != -1):
                rightChild = Binary(rightChildData)
                currentNode.right = rightChild
                q.put(rightChild)
        return root


    def printTree(self, root):
        if(root == None):
            return 
        print(root.data, end = ":")
        if(root.left != None):
            print("L", root.left.data, end = ",")
        if(root.right != None):
            print("R", root.right.data)
        print()
        self.printTree(root.left)
        self.printTree(root.right)

    def minTree(self, root):
        if(root == None):
            return 100000
        leftMin = self.minTree(root.left)
        rightMin = self.minTree(root.right)
        return min(leftMin, rightMin, root.data)

    def maxTree(self, root):
        if(root == None):
            return -100000
        leftMax = self.maxTree(root.left)
        rightMax = self.maxTree(root.right)
        return max(leftMax, rightMax, root.data)

    def isBST(self, root):
        if(root == None):
            return True
        leftMax = self.maxTree(root.left)
        rightMin = self.minTree(root.right)
        if(root.data >= rightMin or root.data <= leftMax):
            return False
        isLeftBST = self.isBST(root.left)
        isRightBST = self.isBST(root.right)
        return isLeftBST == isRightBST

    def searchTree(self, root, val):
        if(root == None):
            return False
        if(root.data == val):
            return True
        elif(root.data > val):
            return self.searchTree(root.left, val)
        else:
            return self.searchTree(root.right,val)
        




bt = BinaryDetails()
root = bt.takeInput()
bt.printTree(root)
#print(bt.isBST(root))
print(bt.searchTree(root, 100))
