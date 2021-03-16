

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def takeInput(self):
        pass

    def printTree(self, root):
        pass

    def buildTreeinorderPreorder(self, pre, inorder):
        if(len(pre) == 0):
            return None
        rootData = pre[0]
        root = Node(rootData)
        rootIndexInorder = -1
        for i in range(0, len(inorder)): 
            if(inorder[i] == rootData):
                rootIndexInorder = i
                break
        if(rootIndexInorder == -1):
            return None

        leftInorder = inorder[0 : rootIndexInorder]
        rightInorder = inorder[rootIndexInorder + 1 :]

        lenLeftSubtree = len(leftInorder)
        leftPreorder = pre[1 : lenLeftSubtree + 1]
        rightPreorder = pre[lenLeftSubtree + 1 :]

        leftChild = self.buildTreeInorderPreorder(leftPreorder, leftInorder)
        rightChild = self.buildTreeInorderPreorder(rightPreorder, rightInorder)

        root.left = leftChild
        root.right = rightChild

        return root














        
        
                
