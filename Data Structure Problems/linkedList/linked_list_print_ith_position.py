

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        

class LL:
    def IthPrint(self, head, pos):
        if(pos < 0 or pos > self.lengthLL(head)):
            return head
        count = 0
        curr = head
        prev = None
        while(count < pos):
            prev = curr
            curr = curr.next
            count += 1
        if(pos != 0):
            return prev.next.data
        else:
            return head.data

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
                tail.next=  newNode
                tail = newNode
        return head

    def lengthLL(self, head):
        count = 0
        while(head != None):
            count += 1
            head = head.next
        return count

    def printLL(self, head):
        while(head != None):
            print(head.data, "--->", end = " ")
            head = head.next
        print("None")
        return



node = LL()
head = node.takeInput()
node.printLL(head)
print(node.IthPrint(head, 0))
print(node.IthPrint(head, 3))
