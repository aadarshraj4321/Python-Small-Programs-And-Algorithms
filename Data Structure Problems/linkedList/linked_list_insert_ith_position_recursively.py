

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LL:
    def insertValRec(self, head, pos, val):
        if(pos < 0):
            return head
        if(pos == 0):
            newNode = Node(val)
            newNode.next = head
            return newNode
        if(head is None):
            return None
        smallHead = self.insertValRec(head.next, pos - 1, val)
        head.next = smallHead
        return head
        
    def takeInput(self):
        userInput = [int(ele) for ele in input().split()]
        head = None
        tail = None
        for val in userInput:
            if(val == -1):
                break
            newNode = Node(val)
            if(head == None):
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
head = node.insertValRec(head, 3, 100)
node.printLL(head)
head = node.insertValRec(head, 0, 200)
node.printLL(head)





