# Python program to find the inroder successor in a BST
 
# A binary tree node 
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key 
        self.parent = None
        self.left = None
        self.right = None
 
 
class BstTree:
    def __init__(self, data):
        self.root= Node(data)
        
    def inOrderSuccessor(self, node):
        
        #if there is a right child of node then succ is there
        if node:
            print "Parent "+str(node.parent)
            if node.right:
                return leftMostChild(node.right)
                
            p = node.parent
            while p:
                if node != p.right:
                    break
                node = p
                p = p.parent
            return p
    def leftMostChild(self, node):
        currentnode = node
        while currentNode:
            if currentNode.left is None:
                break
            currentNode = currentNode.left
        
        return currentNode
                    
    def insert( self, node, data):
 
        # 1) If tree is empty then return a new singly node
        if node is None:
            return Node(data)
        else:
        
            # 2) Otherwise, recur down the tree
            if data <= node.data:
                temp = insert(node.left, data)
                node.left = temp 
                temp.parent = node
            else:
                temp = insert(node.right, data)
                node.right = temp 
                temp.parent = node
         
            # return  the unchanged node pointer
            return node
        
def inOrderSuccessor(root, n):
     
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)
 
    # Step 2 of the above algorithm
    p = n.parent
    while( p is not None):
        if n != p.right :
            break
        n = p 
        p = p.parent
    return p
 
# Given a non-empty binary search tree, return the 
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current is not None):
        if current.left is None:
            break
        current = current.next
 
    return current
 
 
# Given a binary search tree and a number, inserts a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid 
# using reference parameters)
def insert( node, data):
 
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:
        
        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp 
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp 
            temp.parent = node
         
        # return  the unchanged node pointer
        return node
 
 
# Driver progam to test above function
root =None
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);  
root = insert(root, 14);    
temp = root.left.right.right 
 
succ = inOrderSuccessor( root, temp)
if succ is not None:
    print "\nInorder Successor of %d is %d " \
            %(temp.data , succ.data)
else:
    print "\nInorder Successor doesn't exist"
# Creating the tree given in the above diagram 

node = tree.root.left.right.right
succ = tree.inOrderSuccessor( node)
if succ is not None:
    print "\nInorder Successor of %d is %d " \
            %(node.data , succ.data)
else:
    print "\nInorder Successor doesn't exist"