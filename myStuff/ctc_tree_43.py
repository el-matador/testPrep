#Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def preorder(tree_node):
    if tree_node:
        print tree_node.value
        preorder(tree_node.left)
        preorder(tree_node.right)
        
def postorder(tree_node):
    if tree_node:
        
        preorder(tree_node.left)
        preorder(tree_node.right)
        print tree_node.value
        
def inorder(tree_node):
    if tree_node:
        
        preorder(tree_node.left)
        print tree_node.value
        preorder(tree_node.right)
        
        
def addToTree( arrayList, start, end):
    if end<start:
        return None
    mid = (start+end)/2
        
    tree_node = Node(arrayList[mid])
    tree_node.left = addToTree(arrayList, start, mid-1)
    tree_node.right = addToTree(arrayList, mid + 1, end)
    return tree_node
    
arrayList = [1,2,3,4,5,6,7,8,9]


root_tree = addToTree(arrayList,0,len(arrayList)-1)

print "Pre Order---"
inorder(root_tree)

