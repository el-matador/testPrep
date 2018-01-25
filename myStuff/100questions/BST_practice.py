# Definition for a  binary tree node
class BSTNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.mystack = []
        self.pushem(root)
        print "exiting init"
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.mystack)==0:
            return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        temp = self.mystack[-1]
        self.mystack.pop()
        if temp.right:
         self.pushem(temp.right)
        return temp.val
    def pushem(self,A):
        while(A):
            print A.val
            self.mystack.append(A)
            A=A.left
            
        
# Your BSTIterator will be called like this:
root = BSTNode(15)
root.left = BSTNode(8)
root.left.left = BSTNode(4)
root.left.right = BSTNode(10)
root.left.left.left = BSTNode(1)
root.left.left.right = BSTNode(5)
root.left.right.left = BSTNode(9)
root.right= BSTNode(20)
root.right.left = BSTNode(16)
root.right.right = BSTNode(22)

i = BSTIterator(root)
while i.hasNext(): print i.next(),

# Python program to construct tree using inorder and 
# preorder traversals
 
# A binary tree node 
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of inStrt and inEnd should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTree(inOrder, preOrder, inStrt, inEnd):
     
    if (inStrt > inEnd):
        return None
 
    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
 
    # If this node has no children then return
    if inStrt == inEnd :
        return tNode
 
    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)
     
    # Using index in Inorder Traversal, construct left 
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)
 
    return tNode
 
def buildTree2(inOrder, postOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None
    #print buildTree2.preIndex
    tNode = Node(postOrder[buildTree2.preIndex])
    buildTree2.preIndex -=1
    
    # If this node has no children then return
    if inStrt == inEnd :
        return tNode
        
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)
    
    tNode.right = buildTree2(inOrder, postOrder, inIndex+1, inEnd)
    tNode.left = buildTree2(inOrder, postOrder, inStrt, inIndex-1)
    
    return tNode
    
    
# UTILITY FUNCTIONS
# Function to find index of vaue in arr[start...end]
# The function assumes that value is rpesent in inOrder[]
 
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i
 
def printInorder(node):
    if node is None:
        return
    print node.data,
    # first recur on left child
    printInorder(node.left)
     
    #then print the data of node
    
 
    # now recur on right child
    printInorder(node.right)
     
# Driver program to test above function
#inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
#preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
postOrder = ['B', 'D', 'E', 'C', 'F','A']
inO = [4, 8, 2, 5, 1, 6, 3, 7]
pO = [8, 4, 5, 2, 6, 7, 3, 1]
# Static variable preIndex
buildTree2.preIndex = len(inO) -1
root = buildTree2(inO, pO, 0, len(inO)-1)
 
# Let us test the build tree by priting Inorder traversal
print "Inorder traversal of the constructed tree is"
printInorder(root)