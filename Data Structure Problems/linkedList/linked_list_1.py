

class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None
        


a = Node(13)
b = Node(15)
a.nextNode = b

print(a.data)
print(b.data)
print(a.nextNode.data)
#print(a.nextNode)
#print(a)
