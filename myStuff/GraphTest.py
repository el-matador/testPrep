from collections import defaultdict
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        
        
    #function to add edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    #print the BFS of graph from vertex s
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
    
    
    
    
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
        
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def bfs(g,start):
        start.setDistance(0)
        start.setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
    
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
        
        
g.dfs()
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is Breadth First Traversal (starting from vertex)"
g.BFS(0)











class GraphNode:
  def __init__(self,value):
    self.nodeValue = value
    self.neighbours = []
    
class Graph:
  def __init__(self,v):
    self.vertices = v

  def bfs(self,nodeObject):
    #mark all the nodes as not visted
    visited= [False]*(self.vertices)
    queue = []
    
    cloneGraph = None
    nodeMap = {}
    

    #add the node to queue
    queue.append(nodeObject)
    visited[nodeObject.nodeValue-1]= True
    while queue:
      tempObject = queue.pop()
      #print "Popping :",tempObject.nodeValue
      
      if tempObject.nodeValue not in nodeMap:
        cloneGraph = GraphNode(tempObject.nodeValue)
        nodeMap[cloneGraph.nodeValue] = cloneGraph
      else:
        cloneGraph = nodeMap[tempObject.nodeValue]
        
      for neighbor in tempObject.neighbours:
        if neighbor.nodeValue in nodeMap:
            cloneGraph.neighbours.append(nodeMap[neighbor.nodeValue])
        else:
            tempNode = GraphNode(neighbor.nodeValue)
            nodeMap[tempNode.nodeValue] = tempNode
            cloneGraph.neighbours.append(tempNode)
        
        #print "clone Graph Node",cloneGraph.nodeValue
        #for i in    cloneGraph.neighbours:
          #print i.nodeValue
        
        if visited[neighbor.nodeValue-1]== False:
          queue.append(neighbor)
          visited[neighbor.nodeValue-1]= True
          
    #print nodeMap 
    #for key in nodeMap:
      #print "key ",key
      #print nodeMap[key].neighbours
      
      
      
class GraphNode:
  def __init__(self,value):
    self.nodeValue = value
    self.neighbours = []
    
class Graph:
  def __init__(self,v):
    self.vertices = v

  def bfs(self,nodeObject):
    #mark all the nodes as not visted
    #visited= [False]*(self.vertices)
    queue = []
    
    cloneGraph = None
    nodeMap = {}
    

    #add the node to queue
    queue.append(nodeObject)
    #visited[nodeObject.nodeValue-1]= True
    while queue:
      tempObject = queue.pop()
      #print "Popping :",tempObject.nodeValue
      
      if tempObject.nodeValue not in nodeMap:
        cloneGraph = GraphNode(tempObject.nodeValue)
        nodeMap[cloneGraph.nodeValue] = cloneGraph
      else:
        cloneGraph = nodeMap[tempObject.nodeValue]
        
      for neighbor in tempObject.neighbours:
        if neighbor.nodeValue in nodeMap:
            cloneGraph.neighbours.append(nodeMap[neighbor.nodeValue])
        else:
            tempNode = GraphNode(neighbor.nodeValue)
            nodeMap[tempNode.nodeValue] = tempNode
            cloneGraph.neighbours.append(tempNode)
            queue.append(neighbor)
        #print "clone Graph Node",cloneGraph.nodeValue
        #for i in    cloneGraph.neighbours:
          #print i.nodeValue
        
        #if visited[neighbor.nodeValue-1]== False:
          #queue.append(neighbor)
          #visited[neighbor.nodeValue-1]= True
          
    #print nodeMap 
    for key in nodeMap:
      print "key ",key
      print nodeMap[key].neighbours
      
    
      

gNode1 = GraphNode(1)
gNode2 = GraphNode(2)
gNode3 = GraphNode(3)
gNode4 = GraphNode(4)
gNode1.neighbours=[gNode2,gNode3]
gNode2.neighbours=[gNode3,gNode4,gNode1]
gNode3.neighbours=[gNode1,gNode4,gNode2]
gNode4.neighbours=[gNode2,gNode3]

g = Graph(4)
g.bfs(gNode1)
    
    
    
    
    
    
    from collections import defaultdict

class Graph:
  def __init__(self,v):
    self.value = v
    self.adjacentVertex = defaultdict(list)
    
    self.longestPath =0
    self.vertices = 0
    
  def addEdge(self,u,v):
    self.adjacentVertex[u].append(v)

  def dfs(self,v,visited,maxP):
    print v,visited,maxP
    visited[v]= True
    leafNode = v
    maxPath = maxP
    maxP +=1
    for i in self.adjacentVertex[v]:
      if visited[i]==False:
        tempPath,tempNode = self.dfs(i,visited,maxP)
        if tempPath>maxPath:
          maxPath=tempPath
          leafNode = tempNode
          

    
    return maxPath,leafNode
    
    
  def findLongestPath(self,rootNode):
    visited = [False]*(self.vertices)

    pathSum,node = self.dfs(rootNode,visited,0)
    print pathSum,node
    
    





A1 = [-1, 0, 0, 0,3]
A = [2,2,-1,2,3]

g = Graph(len(A))
g.vertices = len(A)


rootNode = None
for index in range(len(A)):
    if A[index]==-1:
      #this is root
      rootNode = index
    else:
      g.addEdge(A[index],index)
      g.addEdge(index,A[index])
      
print g.adjacentVertex
g.findLongestPath(rootNode)
    