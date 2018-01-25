from collections import defaultdict

class Node:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self, item = None): 
        self.root = Node(item)

    def printTree(self):
        if self.root:
            self._printPreOrder(self.root)
    def _printPreOrder(self,node):
        if node:
            print node.value
            self._printPreOrder(node.left)
            self._printPreOrder(node.right)



class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}  #map of vertext objects with thier weight
    
    def addNeighbor(self,nbr,weight):
        self.connectedTo[nbr]=weight

class Graph:
    def __init__(self):
        self.vertList = []
        self.numOfvertices = 0
        self.graph = defaultdict(list) # for directed graph map
    
    def addEdge(self,u,v):
        #u and v are node values without weight
        self.graph[u].append(v)

    def bfs(self,u):
        #starting node from u. search all the connected nodes.
        
        # Mark all the vertices as not visited
        #print self.graph
        visited = [False]*(len(self.graph))
        print visited
        
        #create a queue for BFS
        queueList = []
        
        #Mark the source node as visited and enque it
        queueList.append(u)
        visited[u] = True
        #print queueList
        while queueList:
            # Dequeue a vertex from queue and print it
            s= queueList.pop(0)
            print s
            
            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for vert in self.graph[s]:
                if visited[vert]!=True:
                    visited[vert]=True
                    queueList.append(vert)
    
    def DFSUtil(self,v, visited ):
        # Mark the current node as visited and print it
        visited[v]= True
        print v
        # Recur for all the vertices adjacent to this vertex
        for node in self.graph[v]:
            if visited[node] == False:
                self.DFSUtil(node, visited)
    
    # The function to do DFS traversal
    def DFS(self,v):
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))
        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v,visited)
            
    def bfsVertex(self, vertexObject):
        if vertexObject in self.vertList:
            return
        

#set up graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)

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

#print tree.isBanalanced()
#tree.printTree()