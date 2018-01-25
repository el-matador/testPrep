from collections import defaultdict
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        

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
            
    def deleteNode(self, item):
        currentNode = self.head
        #print currentNode.next
        print "---"
        if currentNode.data == item:
            self.head = currentNode.next
            #del(currentNode)
            return
        
        while currentNode.next != None:
            if currentNode.next.next == None:
                currentNode.next = None
                return
            elif currentNode.next.data == item:
                currentNode.next = currentNode.next.next
                #del(currentNode.next)
            currentNode = currentNode.next
                
            
    def removeDups(self):
        #without buffer
        current = second = self.head
        while current is not None:
            while second.next is not None:   # check second.next here rather than second
                if second.next.data == current.data:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next
        
    def deleteDups(self):
        previousNode = self.head
        nodeMap = []
        #nodeMap[previousNode.data] = True
        nodeMap.append(previousNode.data)
        currentNode = previousNode.next
        while currentNode:
            if currentNode.data in nodeMap:
                previousNode.next = currentNode.next
                
            else:
                #nodeMap[currentNode.data] = True
                nodeMap.append(currentNode.data)
                previousNode = currentNode

            currentNode = currentNode.next
        
        print nodeMap
        

mylist = LinkedList()
mylist.addNode(19)
mylist.addNode(11)
mylist.addNode(15)
mylist.addNode(12)
mylist.addNode(13)
mylist.addNode(15)
mylist.addNode(11)
mylist.addNode(11)
mylist.printLinkedList()
print "---"
mylist.deleteDups()
mylist.printLinkedList()