

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None



class LL:
    
    def insertVal(self, head, pos, val):
        if(pos < 0 or pos > self.lengthLL(head)):
            return head
        count = 0
        curr = head
        prev = None
        while(count < pos):
            prev = curr
            curr = curr.next
            count += 1
        newNode = Node(val)
        if(prev is None):
            head = newNode
        else:
            prev.next = newNode
        newNode.next = curr
        return head
        
    def lengthLL(self, head):
        count = 0
        while(head != None):
            head = head.next
            count += 1
        return count
    
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
head = node.insertVal(head, 3, 10)
node.printLL(head)
head = node.insertVal(head, 0, 20)
node.printLL(head)
