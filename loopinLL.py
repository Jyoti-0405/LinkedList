class Node:
    def __init__(self, data ):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNeighbour(self, src, dest):
        src.next = dest

    def setCycle(self, startPos):
        counter = 1
        temp = self.head
        startElem = None
        while(temp):
            temp = temp.next #pointing to next node
            counter += 1
            if (counter == startPos):#checking if next node is equalt to the index
                startElem = temp #I set the next element to startElem variable
            if (temp.next == None): #I check if next elment is null
                temp.next = startElem #I set next elment as the indexed element
                break

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            break
    def detectloop(self):
        nodes_seen = set()
        temp = self.head
        flag = False
        while(temp):
            nodes_seen.add(temp)
            temp = temp.next
            if temp in nodes_seen:
                flag = True
                break
        return flag
list = LinkedList()
list.head = Node(22)
first = Node(90)
second = Node(33)
third = Node(33)
fourth = Node(43)

list.addNeighbour(list.head, first)
list.addNeighbour(first, second)
list.addNeighbour(second, third)
list.addNeighbour(third, fourth)
list.setCycle(2)

if (list.detectloop()):
    print("loop exists")
else:
    print("loop doesn't exist")


        