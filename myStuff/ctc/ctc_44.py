from collections import defaultdict
class Node:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self, data):
        self.root= Node(data)
        self.nodeListLevelMap = defaultdict(list)
        self.currentLevel = 0
        
    def heightOfTree(self,node):
        if node is None:
            return 0
        leftHeight = self.heightOfTree(node.left)
        rightHeight = self.heightOfTree(node.right)
        
        return 1+ max(leftHeight ,rightHeight)
        
    def traverseNodes(self,node,l):
        if node is None:
            return
        if l == 1:
            #add nodes at this level to map
            self.nodeListLevelMap[ self.currentLevel].append(node.value)
            #print node.value
        elif l >1:
            self.traverseNodes(node.left, l-1)
            self.traverseNodes(node.right, l-1)
            
    def createLinkedList(self):
        if self.root is None:
            return None
        treeheight = self.heightOfTree(self.root)
        self.currentLevel = 1
        self.nodeListLevelMap[ self.currentLevel].append(self.root)
        
        for level in range(2,treeheight +1):
            self.currentLevel = level
            
            for node in self.nodeListLevelMap[self.currentLevel-1]:
                if node.left:
                    self.nodeListLevelMap[ self.currentLevel].append(node.left)
                if node.right:
                    self.nodeListLevelMap[ self.currentLevel].append(node.right)
        print self.nodeListLevelMap
        for level in self.nodeListLevelMap:
            for node in self.nodeListLevelMap[level]:
                print node.value
                
    
    def createLinkedListOfNodes(self):
        if self.root is None:
            return None
        treeheight = self.heightOfTree(self.root)
        for level in range(1,treeheight +1):
            self.currentLevel = level
            self.traverseNodes(self.root, level)
            
        print self.nodeListLevelMap

# Set up tree


tree = Tree(15)
tree.root.left = Node(8)
tree.root.left.left = Node(4)
tree.root.left.right = Node(10)
tree.root.left.left.left = Node(1)
tree.root.left.left.right = Node(2)
tree.root.left.right.left = Node(9)
tree.root.right= Node(20)
tree.root.right.left = Node(16)
tree.root.right.right = Node(22)
#print tree.heightOfTree(tree.root)
tree.createLinkedListOfNodes()
