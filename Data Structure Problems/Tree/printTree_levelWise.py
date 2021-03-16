from queue import Queue as q

class Binary:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryDetails:
    def printTree(self, root):
        if(root == None):
            return None
        print(root.data, end = ":")
        if(root.left != None):
            print("L", root.left.data, end = ",")
        if(root.right != None):
            print("R", root.right.data)
        print()
        self.printTree(root.left)
        self.printTree(root.right)

    def takeInput(self):
        rootData = int(input())
        qu = q()
        if(rootData == -1):
            return None
        root = Binary(rootData)
        qu.put(root)
        while(not(qu.empty())):
            currentNode = qu.get()
            print("Enter left child of ", currentNode.data)
            leftChildData = int(input())
            if(leftChildData != -1):
                leftChild = Binary(leftChildData)
                currentNode.left = leftChild
                qu.put(leftChild)
            print("Enter right child of ", currentNode.data)
            rightChildData = int(input())
            if(rightChildData != -1):
                rightChild = Binary(rightChildData)
                currentNode.right = rightChild
                qu.put(rightChild)
        return root

    def printLevelWise(self, root):
        if(root == None):
            return None
        qu = q()
        qu.put(root)
        while(not(qu.empty())):
            currentNode = qu.get()
            print(currentNode.data)
            if(root.left != None):
                currentNode.left = root.left.data
                qu.put(root.left.data)
            if(root.right != None):
                currentNode.right = root.right.data
                qu.put(root.right.data)
                


bt = BinaryDetails()
root = bt.takeInput()
#bt.printTree(root)
bt.printLevelWise(root)
