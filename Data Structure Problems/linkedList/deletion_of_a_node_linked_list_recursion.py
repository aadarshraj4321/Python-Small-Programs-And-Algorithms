
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LL:

    def deleteNodeRec(self, head, val):
        if(val < 0):
            return head
        if(val == 0):
            return head.next
        if(head == None):
            return None

        dele = self.deleteNodeRec(head.next, val - 1)
        head.next = dele
        return head
    
    def takeInput(self):
        userInput = [int(ele) for ele in input().split()]
        head = None
        tail = None
        for val in userInput:
            if(val == -1):
                break
            newNode = Node(val)
            if(head is None):
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head

    def printLL(self, head):
        while(head != None):
            print(head.data, "--->", end = " ")
            head = head.next
        print("None")
        return


node = LL()
head = node.takeInput()
node.printLL(head)
head = node.deleteNodeRec(head, 3)
node.printLL(head)
