class Node:
    def __init__(self, data):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(head):
        head = None
    def printlist(head):
        printval = head
        while(printval):
            print(printval.data)
            printval = printval.next
    
    def rotateList(head,k):
        if not head:
            return None
        lastElement = head
        length = 1
        while(lastElement.next):
            lastElement = lastElement.next
            length+=1

        k = k%length
        lastElement.next = head
        tempNode = head
        for _ in range(length-k-1):
            tempNode = tempNode.next
        answer = tempNode.next
        tempNode.next = None

        return answer
list1 = LinkedList
list1.head = Node(3)
list1.head.next = Node(6)
list1.head.next.next = Node(72)
list1.head.next.next.next = Node(89)
list1.head.next.next.next.next = Node(12)
print("List before rotation")
list1.printlist(list1.head)
list1.rotateList(list1.head, 2 )
print("List After rotation")
list1.printlist(list1.head)



    