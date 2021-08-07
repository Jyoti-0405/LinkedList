class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp= self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            break
    def push(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
    def Detectloop(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head.next
        while slow!= fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            break
        return True


list = LinkedList()
list.push(10)
list.push(11)
list.push(12)
list.push(13)
#creating a loop for checking
list.head.next.next.next.next = list.head
if (list.Detectloop()):
    print("loop found")
else:
    print("loop not found")
