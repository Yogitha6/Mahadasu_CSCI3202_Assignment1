class GraphImplementation:

	def __init__(self):
	    self.graph = {}
	    self.edges = []

	def isVertex(self, value):
	    if self.graph!=None:
	        return self.graph.has_key(value)
	    else:
		    return None

	def addVertex(self, value):
	    if self.isVertex(value) != True :
		    self.graph[value]=[]
	    else:
		    print "Vertex already exists"
	
	def addEdge(self, value1, value2):
	    if self.isVertex(value1) == True and self.isVertex(value2) == True :
		    self.edges.append({value1,value2})
		    self.graph[value1].append(value2)
		    self.graph[value2].append(value1)
	    else:
		    print "One ore more vertices not found %s and %s" %(value1,value2) 
	
	def findVertex(self, vertex):
	    if self.isVertex(vertex) == True:
		    print "The key values of the adjacent vertices to the vertex %s are %s:" %(vertex,self.graph.get(vertex))
	    else:
		    print "Vertex not found"
