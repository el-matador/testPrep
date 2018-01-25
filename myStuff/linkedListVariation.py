from collections import defaultdict
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.random = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        #self.duplicateMap = defaultdict()
        
    def addNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def printLinkedList(self):
        currentNode = self.head
        
        while currentNode:
            print currentNode.data
            currentNode = currentNode.next
            
    def createClone(self):
        #create a new list object
        
        currentNode = self.head
        cloneList = LinkedList()
        
        while currentNode:
            cloneList.addNode(currentNode.data)
            currentNode = currentNode.next

        return cloneList


mylist = LinkedList()
mylist.addNode(4)
mylist.addNode(3)
mylist.addNode(2)
mylist.addNode(1)

mylist.printLinkedList()
#print "Head of Original List",mylist.head
print "Cloned List Object",mylist.createClone()

print "Cloned List -"
mylist.createClone().printLinkedList()

class Node:
    def __init__(self,item):
      self.data= item
      self.next = None
      

def reverseList(root):
  if root is None:
    return None
  #need to store list elemenets
  parsedList = []
  currentNode = root
  
  while currentNode:
    parsedList.append(currentNode)
    currentNode = currentNode.next
  head = parsedList[-1]
  #print parsedList
  while parsedList:
    tempNode = parsedList.pop()
    #print tempNode.data
    if parsedList:
      tempNode.next = parsedList[-1]
    else:
      tempNode.next = None
    
  currentNode = head
  
  while currentNode:
      print currentNode.data
      currentNode = currentNode.next
      
def reverseList1(root):
  if root is None:
    return None
    
  prevNode = None
  currentNode = root
  
  while currentNode: 
    nextNode = currentNode.next
    currentNode.next = prevNode
    prevNode = currentNode
    currentNode = nextNode
  
  currentNode = prevNode
  while currentNode:
      print currentNode.data
      currentNode = currentNode.next
  
def reverse(root  ):
  if root is None:
    return None
    
  prevNode = None
  currentNode = root
  
  while currentNode: 
    nextNode = currentNode.next
    currentNode.next = prevNode
    prevNode = currentNode
    currentNode = nextNode
  
  headNode = prevNode
  tailNode = root
  return (prevNode.data,root.data)
  
  
def reverseByGroup(head,k):
  cuurent = head
  prev = None
  next = None
  count = 0
  while (count<k and cuurent):
    next = cuurent.next
    cuurent.next = prev
    prev = cuurent
    cuurent = next
    count +=1
  if next:
    head.next = reverseByGroup(next,k)
    
  return prev
  
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)
root.next.next.next.next.next.next.next.next = Node(9)
node = reverseByGroup(root,3)
currentNode = node
  
while currentNode:
      print currentNode.data
      currentNode = currentNode.next
    