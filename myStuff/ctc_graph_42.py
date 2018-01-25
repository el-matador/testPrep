from collections import defaultdict

#Given a directed graph, design an algorithm to  find out whether there is a route be- tween two nodes.

#We start with one of the two nodes and, during traversal, check if the other node is found.

class Graph:
    def __init__(self):
        #self.vertexMap = defaultdict(list)
        self.vertexMap = {}
        self.searchPath = []
        
    def addEdge(self, u,v):
        if u not in self.vertexMap:
            self.vertexMap[u]=[]
        self.vertexMap[u].append(v) # u: [v,]
        
    def dfsSearchPath(self, u,v):
        #
        visited = [False]*len(self.vertexMap)
        
        
        print "Initial Path :"+str(self.searchPath)
        return self.searchPathUtil(u,v,visited)
        
        
        
    def searchPathUtil(self,u,v,visited):
        visited[u] = True
        
        for node in self.vertexMap:
                if u == v:
                    return True
                if visited[node] ==False:
                    self.searchPathUtil(node,v,visited)
                    
        return False
                
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

#set up directed graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print g.dfsSearchPath(1,0)