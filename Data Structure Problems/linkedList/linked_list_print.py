


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LL:
    def printLL(self, head):
        while(head is not None):
            print(head.data, "--->", end = " ")
            head = head.next
        print("None")
        return



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ll = LL()
ll.printLL(node1)
        
