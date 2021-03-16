


class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None

class ReverseLL:
    def takeInput(self):
        inputList = [int(i) for i in input().split()]
        head = None
        tail = None
        for cd in inputList:
            if(cd == -1):
                break
            newNode = Node(cd)
            if(head is None):
                head = newNode
                tail = newNode
            else:
                tail.nextNode = newNode
                tail = newNode
        return head     
    
    def printLL(self, head):
        while(head is not None):
            print(str(head.data) + "--->", end="")
            head = head.nextNode
        print(None)
        return
    
def RecursivereverseLinked(head):
    if(head is None or head.nextNode is None):
        return head
    smallHead = RecursivereverseLinked(head.nextNode)
    curr = smallHead
    while(curr.nextNode is not None):
        curr =  curr.nextNode
    curr.nextNode = head
    head.nextNode = None
    return smallHead


reverse = ReverseLL()
head = reverse.takeInput()
reverse.printLL(head)
newHead = RecursivereverseLinked(head)
reverse.printLL(newHead)










    
        
