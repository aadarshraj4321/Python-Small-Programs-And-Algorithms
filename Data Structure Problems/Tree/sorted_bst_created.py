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

    def sortedBinary(self, data):
        lenData = len(data)
        finalData = sum(data) / lenData
        if(finalData == -1):
            return None
        root = Binary(finalData)
        leftSlice = data[:finalData]
        rightSlice = data[finalData + 1:]

        root.left = leftSlice
        root.right = rightSlice
        self.sortedBinary(root.left)
        self.sortedBinary(root.right)
        return root
        


bt = BinaryDetails()
root = bt.takeInput()
bt.printTree(root)
bt.sortedBinary([1, 2, 3, 4, 5, 6, 7])
         
