class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval != None:
            print(printval.dataval)
            printval=printval.nextval
    def addathead(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    def addattail(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval= NewNode
            return 
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
    def addatindex(self,pos_node,newdata):
        if pos_node is None:
            print("Node not present")
            return
        NewNode = Node(newdata)
        NewNode.nextval = pos_node.nextval
        pos_node.nextval = NewNode
        
    def deleteatindex(self,key):
        temp = self.headval
        if (temp is not None):
            if temp.dataval == key:
                self.headval = temp.nextval
                temp = None
                return
        while(temp is not None):
            if temp.dataval==key:
                break
            prev = temp
            temp = temp.nextval
        if(temp == None):
            return
        prev.nextval = temp.nextval
        temp = None
        
list1 = LinkedList()
list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Friday")
list1.headval.nextval = e2
e2.nextval = e3
list1.addathead("Sunday")
list1.addattail("Saturday")
list1.addatindex(list1.headval.nextval.nextval,"Wednesday")
list1.deleteatindex("Saturday")
list1.printlist()
