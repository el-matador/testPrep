#Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is de ned 
to be a tree such that no two leaf nodes di er in distance from the root by more than one.

class Node:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self, data):
        self.root= Node(data)
    
    def maxDepth(self,node):
        if node:
            return 1+ max(self.maxDepth(node.left), self.maxDepth(node.right))
        else:
            return 0
            
    def minDepth(self,node):
        if node:
            return 1+ min(self.minDepth(node.left), self.minDepth(node.right))
        else:
            return 0
            
    def isBanalanced(self):
        maxD = self.maxDepth(self.root)
        minD = self.minDepth(self.root)
        print maxD
        print minD
        if maxD - minD <=1:
            return True
        else:
            return False
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Set up tree
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.left.left = Node(9)

print tree.isBanalanced()

print tree.print_tree()