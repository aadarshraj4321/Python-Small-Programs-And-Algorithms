
class Binary:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None



class BinaryDetails:
    def isBalanced(self, root):
        if(root == None):
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if(left - right > 1 or right - left > 1):
            return False
        isLeft = self.isBalanced(root.left)
        isRight = self.isBalanced(root.right)
        if(isLeft and isRight):
            return True
        else:
            return False

    def height(self, root):
        if(root == None):
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        longest = max(left, right)
        return 1 + longest


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
        if(rootData == -1):
            return None
        root = Binary(rootData)
        left = self.takeInput()
        right = self.takeInput()
        root.left = left
        root.right = right
        return root

##    def bst(self, root):
##        if(root == None):
##            return True
##        if(root.left.data < root.data and root.right.data > root.data):
##            return True
##        else:
##            return False
##        root.left = self.bst(root.left)
##        root.right = self.bst(root.right)

        

    
bt = BinaryDetails()
root = bt.takeInput()
bt.printTree(root)
print(bt.isBalanced(root))
print(bt.bst(root))






    
