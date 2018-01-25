# Python program to check if a binary tree is bst or not
 
INT_MAX = 4294967296
INT_MIN = -4294967296
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
 
# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    #print "mini maxi :",mini,maxi
    #print "node data :",node.data
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))
 


def searchBST(node,item, minDiff, minDiffNodeValue):
    if not node:
        return None
    #print node.data,minDiff
    if node.data == item:
            print "Found"
            return node
            
    if minDiff > abs(node.data - item):
        minDiff = abs(node.data - item)
        #minDiffNodeValue = node.data
    
    if item < node.data:
            return searchBST(node.left,item,minDiff, node.data)
    else :
            return searchBST(node.right,item, minDiff, node.data)
             
    return minDiffNodeValue


def minDiff(node,item):
    minDiff = INT_MAX
    minDiffNode = Node(-1)
    
    return searchBST(node,item,minDiff,minDiffNode.data)
    
    
    
    
    
    
# Driver program to test above function
#root = Node(4)
#root.left = Node(2)
#root.right = Node(5)
#root.left.left = Node(1)
#root.left.right = Node(3)
 
root = Node(15)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.left = Node(1)
root.left.left.right = Node(5)
root.left.right.left = Node(9)
root.right= Node(20)
root.right.left = Node(16)
root.right.right = Node(22)

if (isBST(root)):
    print "Is BST"
else:
    print "Not a BST"



print "Node near or tree :",minDiff(root,3 )


