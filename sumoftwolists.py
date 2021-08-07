class Node:
    def __init__(self,data):
        self.data = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data) :
        NewNode = Node(new_data)
        NewNode.next = self.head
        self.head = NewNode
    
    
    

    def sumoftwoLL(self, first, second):
        prev = None
        temp = None
        carry = 0
        while (first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            sum = carry + fdata + sdata
            carry =1 if sum>10 else 0
            sum = sum if sum<10 else sum%10
            temp = Node(sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next =  temp
            
            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry>0:
            temp.next = Node(carry)
    

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    

    

first = LinkedList()
second = LinkedList()

first.head(2)
first.head.next(9)
first.head.next.next(3)
first.head.next.next.next(6)
print("First list:-")
first.printlist()

second.head(5)
second.head.next(4)
second.head.next.next(2)
print("Second list is:-")
second.printlist()
res = LinkedList()
res.sumoftwoLL(2, 5)
print("The Sum is:- ")
res.printlist()





