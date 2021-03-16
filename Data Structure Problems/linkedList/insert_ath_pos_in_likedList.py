
class Node:
    def __init__(self, value):
        self.data = value
        self.nextNode = None


class Solution:
    def takeInput(self):
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



def length(head):
    count = 0
    while(head is not None):
        count += 1
        head = head.nextNode
    return count  


def insertPos(head, i, data):
    if(i < 0 or i > length(head)):
        return head
    count = 0
    curr = head
    prev = None
    while(count < i):
        prev = curr
        curr = curr.nextNode
        count += 1
    newNode = Node(data)
    if(prev is not None):
        prev.nextNode = newNode
    else:
        head = newNode
    newNode.nextNode = curr

    return head


def printLL(head):
    while(head is not None):
        print(str(head.data) + "-->", end="")
        head = head.nextNode
    print(None)
    return


sol = Solution()
a = sol.takeInput()
printLL(a)
a = insertPos(a, 3, 200)
printLL(a)
a = insertPos(a, 0, 400)
printLL(a)
