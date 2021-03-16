


class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None
        

def deleteNode(node):
    while(node.data is not val):
        node = node.nextNode
    node.data = node.nextNode.data
    node.nextNode = node.nextNode.nextNode

def printLL(head):
    while(head is not None):
        print(str(head.data) + "--->", end="")
        head = head.nextNode
    print(None)
    return 



head = Node(1)
b = Node(2)
c = Node(6)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)


head.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = f
f.nextNode = g


printLL(head)
removeValue(head, 6)
printLL(head)


































    
