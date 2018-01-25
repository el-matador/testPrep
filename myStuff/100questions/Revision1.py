https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

https://www.geeksforgeeks.org/longest-path-undirected-tree/

https://www.geeksforgeeks.org/find-closest-element-binary-search-tree/

https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
 
 
# Print nodes at a given level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
        
# Return true if the given tree is a BST and its values
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
 
 
# Use BFS to check path between s and d
 def isReachable(self, s, d):
        # Mark all the vertices as not visited
        visited =[False]*(len(self.vertexMap))
  
        # Create a queue for BFS
        queue=[]
        print self.vertexMap
        print visited
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
  
        while queue:
 
            #Dequeue a vertex from queue 
            n = queue.pop(0)
             
            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True
 
            #  Else, continue to do BFS
            for i in self.vertexMap[n]:
            
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # If BFS is complete without visited d
        return False



#remove duplicates from list
        
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
        nodeMap = {}
        nodeMap[previousNode.data] = True
        currentNode = previousNode.next
        while currentNode:
            if currentNode.data in nodeMap:
                previousNode.next = currentNode.next
                
            else:
                nodeMap[currentNode.data] = True
                previousNode = currentNode

            currentNode = currentNode.next
        
        print nodeMap
        

#find if tree is balanced

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
        #print maxD
        #print minD
        if maxD - minD <=1:
            return True
        else:
            return False

def iterativeInOrderTraversal(self):
        result = []
        stack = []
        currentNode = self.root
        
        while currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left
        
        while stack:
            currentNode = stack.pop()
            result.append(currentNode.value)
            if currentNode.right:
                currentNode = currentNode.right
                while currentNode:
                    stack.append(currentNode)
                    currentNode = currentNode.left
                    
        return result

def itPreorderTraversal(root):
  result = []
  stack = []
  
  stack.append(root)
  
  while stack:
    currentNode = stack.pop()
    result.append(currentNode.val)
    if currentNode.right:
      stack.append(currentNode.right)
      
    if currentNode.left:
      stack.append(currentNode.left)
      
  return result
  
# A iterative function to do postorder traversal of 
# a given binary tree
def postOrderIterative(root):
         
    # Check for empty tree
    if root is None:
        return
 
    stack = []
     
    while(True):
         
        while (root):
             # Push root's right child and then root to stack
             if root.right is not None:
                stack.append(root.right)
             stack.append(root)
 
             # Set root as root's left child
             root = root.left
         
        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
            peek(stack) == root.right):
            stack.pop() # Remove right child from stack 
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the 
                             # righ childis processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.data) 
            root = None
 
        if (len(stack) <= 0):
                break
  

def BFS(self, s):
        
        # Mark all the vertices as not visited
        #print self.graph
        visited = [False]*(len(self.graph))
        
        #create a queue for BFS
        queue = []
        
        #Mark the source node as visited and enque it
        queue.append(s)
        visited[s] = True
        
        while queue:
            # Dequeue a vertex from queue and print it
            #print "Queue :"+str(queue)
            s = queue.pop(0)
            print str(s)+"---Vertex"
            
            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for vert in self.graph[s]:
                #print vert
                #print visited
                if visited[vert] !=True:
                    visited[vert] = True
                    queue.append(vert)
            
def DFSUtil(self,v, visited ):
        # Mark the current node as visited and print it
        visited[v]= True
        print v
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
# The function to do DFS traversal
def DFS(self,v):
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))
        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v,visited)


#Reverse a List by k group

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
            
#Build tree from inorder and preorder tree

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
    

# function to get diameter of a binary tree
def diameter(tree):
    dia = 0
    def height_and_dia(tree):
        nonlocal dia
        if not (tree):
            return 0
        lh = height_and_dia(tree.left)
        rh = height_and_dia(tree.right)
        dia = max(dia, lh+rh+1)
        return max(lh, rh)+1

    height_and_dia(tree)
    return dia
	
	
#get the max area from a container
def maxArea(self, A):
        if len(A)<2:
            return 0
    
        maxA = 0
        lh = 0
        rh = len(A)-1
  
        while lh < rh:
            maxA = max(maxA, (rh-lh)* min(A[lh],A[rh]))
            if A[lh] <A[rh]:
                lh +=1 
            else:
                rh -=1 
                
def find_grants_cap(grantsArray, newBudget):
  n = len(grantsArray)
  grantsArray.sort(reverse = True)
  grantsArray.append(0)
  
  sumA = 0
  
  for num in grantsArray:
    sumA += num
    
  surplus = sumA - newBudget
  
  if surplus <=0:
    return grantsArray[0]
  
  for i in range(n):
    surplus -= (i+1)*(grantsArray[i]-grantsArray[i+1])
    
    if surplus <=0:
      break
      
  return grantsArray[i+1] + (-surplus/float(i+1))
  
  
A = [50,20,100,130,167]
print find_grants_cap(A,400)


def minCandy(A):
  n = len(A)
  
  list1 = [0]*n
  minCandy = 0
  print "size",n
  
  for i in range(n):
    if i == 0:
      list1[0]=1
      continue
    if A[i] > A[i-1]:
      list1[i]= list1[i-1] +1
    else:
      list1[i] = 1
  
  for i in range(n-1,-1,-1):
    tempCandy =0
    if i==(n-1):
      tempCandy = list1[n-1]
      list1[n-1] = 1
      minCandy = minCandy + max(list1[n-1],tempCandy)
      continue
    
    tempCandy = list1[i]
    
    if A[i] > A[i+1]:
      list1[i] = list1[i+1] +1 

    else:
      list1[i] =1
      
    minCandy = minCandy + max(list1[i],tempCandy)
      
  return "Minimum Candy",minCandy
  
  



A = [0,1,0,2,1,0,1,3,2,1,2,1]

print minCandy(A)


def findMinSortedArray(A):
  n= len(A)
  
  if n==0:
    return None
  elif n<2:
    return A 
    
  left = 0
  right = n-1
  
  while left <= right:
    
    while A[left] == A[right]:
      left +=1
      
    if (right - left ==1):
      return min(A[left],A[right])
    
    if left ==right:
      return A[left]
      
    mid = left + (right-left)/2
    
    if A[mid] > A[right]:
      #the min element is on the right sub Array
      left = mid
      
    else:
      right = mid
      
  return A[left]


#A=[4, 5, 6, 7, 0, 1, 2]
A=[3,1,2]
A1 =[1, 2, 3, 4]
A2 = [6, 7, 8, 9, 1, 1, 2, 2, 3, 4, 5]
A3 = [6, 7, 8, 9, 1, 2, 3, 3, 4, 4, 5]
A4 = [1,0,0,2]
print findMinSortedArray(A)


def index_equals_value_search(A):
  n = len(A)
  
  left = 0
  right = n-1
  if n==0:
    return -1
  
  if n<2:
    if A[0]==0:
      return 0
    else:
      return -1
  
  lowestIndex  =-1
  while left <=right:
    
    mid = left+ (right - left)/2
    if mid <lowestIndex :
      lowestIndex = mid
      
    if mid == A[mid]:
        lowestIndex = mid
        #return mid
    
    if mid > A[mid]:
      left = mid+1
      
    else:
      right = mid-1
      
  return lowestIndex
    
A = [-8,0,2,5]
A1 =  [-1,0,3,6]
A2 = [5,6,7,8]
A3 = [0,1,2,3,4] # 0
A4 = [-5,0,2,3,10,29]
print index_equals_value_search(A)
    

def findElementSortedArray(A, k):
  
  n = len(A)
  left = 0
  right = n-1
  
  if n==0:
    return -1 
    
  if n<2:
    if A[0] ==k:
      return 0
  
  while left <=right:
    mid = left + (right-left)/2
    #print mid
    print left,right 
    if A[mid] == k:
      return mid
      
    if (A[mid] > A[left]):
      # this part of array is sorted one 
      
      if (k < A[mid]) and (k>=A[left]):
        right = mid -1 
        
      else:
        #the value is in other half
        left = mid + 1 

    else:
      # this part is not sorted
      if (k > A[mid]) and (k<=A[right]):
        left = mid +1 
      else:
        right  = mid -1 
        
  return -1 
  
  
A = [5, 6, 7, 8, 9, 10, 1, 2, 3]

k = 2
print findElementSortedArray(A,3)
      

