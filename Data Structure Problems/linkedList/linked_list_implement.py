

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(node1.data)
print(node1.next.data)
