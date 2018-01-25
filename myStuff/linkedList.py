class Node:
    def __init__(self,item):
        self.data = item
        self.nextNode = None
    
    def setData(self,item):
        self.data = item
    def getData(self):
        return self.data
    def setNextNode(self, newNode):
        self.nextNode = newNode
    def getNextNode(self):
        return self.nextNode
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addNode(self,data):
        newNode = Node(data)
        newNode.setNextNode(self.head)
        self.head = newNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.getData())
            currentNode = currentNode.getNextNode()
            
    def getLengthList(self):
        currentNode = self.head
        size = 0
        while  currentNode != None:
            size +=1
            currentNode = currentNode.getNextNode()
        
        return size
            

def addTwoList(list1,list2):
    
    size1 = list1.getLengthList()#4568
    size2 = list2.getLengthList()#0123
    carryNode = Node(0)# intialize carry with 0
    sum = 0
    size = min(size1,size2)
    print str(size)+" lower size"
    sumList = []
    
    currentNode1 = list1.head
    currentNode2 = list2.head
        
    for index in range(size):
        sum = sum+ currentNode1.data + currentNode2.data + carryNode.data
        carryNode.data = sum%10
        sumList.append(sum)
        
    print sumList
    print carryNode.data
        
    
mylist1 = LinkedList()
mylist1.addNode(1)
mylist1.addNode(2)
mylist1.addNode(3)
mylist1.printLinkedList()

print "Second list"
mylist2 = LinkedList()
mylist2.addNode(4)
mylist2.addNode(5)
mylist2.addNode(6)
mylist2.addNode(8)
mylist2.printLinkedList()

#Question: Given two numbers represented by two linked lists, write a function that returns sum list.
#no extra space
print "Length of List 1"
print mylist1.getLengthList()

print "Length of List 2"
print mylist2.getLengthList()

print "Adding two lists :\n"
addTwoList(mylist1,mylist2)
