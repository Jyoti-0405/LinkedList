class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def addathead(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
    def addattail(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
    def addatindex(self,pos_index, newdata):
        if pos_index is None:
            print("element not present")
            return
        NewNode = Node(newdata)
        NewNode.next = pos_index.next
        pos_index.next = NewNode
        
    def delete(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            if temp == None:
                prev.next = temp.next
                temp = None



list= LinkedList()
list.head = Node(1)
e2 = Node(3)
e3 = Node(4)
list.head.next = e2
e2.next = e3
list.addathead(34)
list.addattail(78)
list.addatindex(list.head.next,222)
list.delete(3)
list.traverse()
