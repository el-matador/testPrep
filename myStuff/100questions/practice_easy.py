# Question1: Add two binary numbers 

#Approach: 1. Make them equal sized by adding 0s at the begining of smaller string.
#Sum = a XOR b XOR c ,  Carry = (a AND b) OR ( b AND c ) OR ( c AND a )

def add_binary_numbers(x,y):
    maxlen = max(len(x), len(y))
    #Normalize lengths
    x = x.zfill(maxlen)
    y = y.zfill(maxlen)
    
    print (x)
    print (y)
    
    result = ''
    carry = 0
    for i in range(maxlen-1, -1, -1):
        first_bit = x[i]
        second_bit = y[i]
        sum = int(first_bit)^int(second_bit)^int(carry)
        result = str(sum)+result
        carry = (int(first_bit) & int(second_bit)) | (int(second_bit) & int(carry)) | (int(carry) & int(first_bit))
        
    return result
    
x= "11001"
y= "101"

#print add_binary_numbers(x,y)

#Question 2 : How to determine if a binary tree is height-balanced

#Approach : the difference of min depth and max depth should not exceed 1

def max_depth_tree(tree_node):
    if tree_node:
        return 1 + max(max_depth_tree(tree_node.left), max_depth_tree(tree_node.right))
    else:
        return 0

def min_depth_tree(tree_node):
    if tree_node:
        return 1 + min(min_depth_tree(tree_node.left), min_depth_tree(tree_node.right))
    else:
        return 0
def is_tree_balanced(root_node):
    if root_node:
        min_d = min_depth_tree(root_node)
        max_d = max_depth_tree(root_node)
        
        if (max_d-min_d) > 1:
            return False
        else:
            return True


#For common use purpose
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
#Question 3: Binary tree level order traversal - non recursive bottom to top and bottom to top

#Approach: find the height of tree. and use stack
def height_tree(tree_node):
    if tree_node:
        return 1+ max(height_tree(tree_node.left), height_tree(tree_node.right))
    else:
        return 0

def print_given_level(tree_node, level):
    
    if tree_node is None:
        return
    elif level == 1:
        #nodeList.append(tree_node.data)
        print tree_node.data
    elif level > 1:
        print_given_level(tree_node.left, level -1)
        print_given_level(tree_node.right, level -1)

def print_level_order_bottom_top(root_node):
    height = height_tree(root_node)
    #print height
    nodeList = []
    for l in range(height,0,-1):
        print_given_level(root_node, l)
        
    #print nodeList

        
root = Node(15)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.left = Node(1)
root.left.left.right = Node(2)
root.left.right.left = Node(9)
root.right= Node(20)
root.right.left = Node(16)
root.right.right = Node(22)
#print_level_order_bottom_top(root)

#question4
# A program to count the number of ways to reach n'th stair
 
# Recursive function used by countWays
def countWaysUtil(n,m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<=m and i<=n:
        res = res + countWaysUtil(n-i, m)
        i = i + 1
    return res
     
# Returns number of ways to reach s'th stair    
def countWays(s,m):
    return countWaysUtil(s+1, m)
     
 
# Driver program
s,m = 4,1
#print "Number of ways =",countWays(s, m)


#Question : Count and Say

#Approach: maintain a count of characters from left while reading the number



def get_chunky(s):
    arr = []
    last = ""
    for ch in s:
        if ch != last:
            arr.append(ch)
        else:
            arr[-1] = str(arr[-1]) + ch
        last = ch
    return arr


def count_and_say(n):
    iterations = int(n)
    print("Will show {} iterations:\n".format(iterations))
    current = "1"
    print(current)
    outputList = []
    outputList.append(current)
    for n in range(iterations-1):
        output = ""
        chunks = get_chunky(current)
        print chunks
        for chunk in chunks:
            output += str(len(chunk)) + chunk[0]
        outputList.append(output)
        current = output

    print outputList
#count_and_say(6)


#delete node from Linked list

def delete( value):
        current = head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                head = current.next


#remove duplicates
def swap(A, pos1, pos2):
    temp = A[pos1]
    A[pos1]=A[pos2]
    A[pos2]=temp

def removeDuplicates(A):
    if len(A) == 0:
        return 0
    end = 0
    print A
    for i in range(1,len(A)):
        if A[i] != A[end]:
            end +=1
            swap(A, i,end)
    print A
    return A[:end + 1]
    


            
A = [1,1,1,2,2,2,2,1,1,1,12,2,2,3,4,5,6,7,7,8]
#print removeDuplicates(A)

#remove all instances of the elemenet from Array

def removeElement(A, item):
    if len(A) ==0:
        return
    endIndex = 0
    print A
    for i in range(0,len(A)):
        if A[i]!=item:
            A[endIndex] = A[i]
            endIndex +=1
        
    return A[:endIndex+1]
    
#print removeElement(A,2)
            

#Question:Program for nth node from the end of a Linked List
#Approach :Print the len of list - n node from the begining of the Linked List

#Question : reverse the number recusive way

def reverseNum(num):
    reverse =0
    while num >0:
        remainder = num%10
        reverse = (reverse * 10) + remainder
        num = num/10
        
    return reverse
    
    
    
#print reverseNum(1234)

def addNum(A,B):
    sum =0
    c =0
    
    size = min(len(A),len(B))
    sumList=[0]*(size)

    for i in range(size-1,-1,-1):
        sum = A[i]+B[i] +c 
        sumList[i]=sum%10
        c=sum/10

    diff = abs(len(A)-len(B))
    
    if diff ==0:
        if c>0:
            sumList.insert(0,c)
    else:
        if len(A) > len(B):
            if c>0:
                
    print sumList
    
    

A =[3,2,3]
B=[9,2,8]
addNum(A,B)

 

class Solution:
    '''       5
                 11
               7   16
                9    25
                 10
    
        Node:
            data (integer)
            left (Node)
            right (Node)
         
    '''
    maxDia = 0
    def height(node):
        if node == None:
            return 0
        
        else:
            lheight = height(node.left)
            rheight = height(node.right)
            
        maxDia = max(maxDia, lheight + rheight + 1)
            
        return max(lheight, rheight) + 1
        
    def diameter(currentNode, maxDiameter=0):
        height(currentNode)
        return maxDia
        
        
        while currentNode:
            
            currentDia = height(currentNode) 
            
            if currentDia > maxDiameter:
                maxDiameter = currentDia
                
            if currentNode.left:
                diameter(currentNode.left, maxDiameter)
                
            if currentNode.right:
                diameter(currentNode.right, maxDiameter)
                
                
        
        
        
    
