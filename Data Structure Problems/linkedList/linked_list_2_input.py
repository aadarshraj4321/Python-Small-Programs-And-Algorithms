
class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None


def printLL(head):
    while(head is not None):
        print(str(head.data) + "------->", end="")
        head= head.nextNode
    print("None")
    return 

def length(head):
    count = 0
    while(head is not None):
        count += 1
        head = head.nextNode
    return count


def insert(node, i, data):
    if(i < 0 or i > length(node)):
        return node 
    count = 0
    prev = None
    curr = node
    while(count< i):
        prev = curr
        curr = curr.nextNode
        count = count + 1
    newNode = Node(data)
    if(prev is not None):
        prev.nextNode = newNode
    else:
        node = newNode
    newNode.nextNode = curr
    return node
    
    



def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentData in inputList:
        if(currentData == -1):
            break
        newNode = Node(currentData)
        if(head is None):
            head = newNode
            tail = newNode
        else:
            tail.nextNode = newNode
            tail = newNode
    return head
        
head = takeInput()
printLL(head)
head = insert(head, 0, 2000)
printLL(head)
