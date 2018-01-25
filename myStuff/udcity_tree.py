class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root:
            new_node = Node(new_val)
            self.insert_node(self.root, new_node)
                
    def insert_node(self,parent_node,new_node):
        if new_node.value < parent_node.value:
            if parent_node.left:
                self.insert_node( parent_node.left, new_node)
            else:
                parent_node.left = new_node
        else:
            if parent_node.right:
                self.insert_node( parent_node.right, new_node)
            else:
                parent_node.right = new_node
            
        

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    
# Set up tree
bst_tree = BST(4)

# Insert elements
bst_tree.insert(2)
bst_tree.insert(1)
bst_tree.insert(3)
bst_tree.insert(5)

# Check search
# Should be True
print bst_tree.search(4)
# Should be False
print bst_tree.search(6)

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
#print tree.search(4)
# Should be False
#print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
#print tree.print_tree()