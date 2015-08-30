class Node:
    def __init__(self):
	    self.key = None
	    self.leftChild = None
	    self.rightChild = None
	    self.parent = None

class TreeImplementation:
    def __init__(self):
	    self.rootnode = None
		
    def searchNode(self, value, currentNode):
		foundNode = None	
		if currentNode.key == value:
		    return currentNode
		if currentNode.leftChild != None:
			foundNode = self.searchNode(value, currentNode.leftChild)
		if currentNode.rightChild != None and foundNode == None:
			foundNode = self.searchNode(value, currentNode.rightChild)
		return foundNode

    def add(self, value, parentValue):
		newnode = Node()
		newnode.key = value
		if self.rootnode == None and parentValue == -1:
		    self.rootnode = newnode
		    print "The root node for this tree is %s" %self.rootnode.key
		else:
		    #search for parentValue - parent node and then add the above newnode as a child
			parentNode = self.searchNode(parentValue, self.rootnode)
			if parentNode != None :
				if parentNode.leftChild == None:
					parentNode.leftChild = newnode
					newnode.parent = parentNode
					print "%s has been assigned as a left child of %s" % (parentNode.leftChild.key,parentNode.key)
				elif parentNode.rightChild == None:
					parentNode.rightChild = newnode
					newnode.parent = parentNode
					print "%s has been assigned as a right child of %s" % (parentNode.rightChild.key,parentNode.key)
				else:
					print "Parent has two children, node not added."
			else:
				print "Parent not found."
				
    def delete(self, value):
		newnode = Node()
		newnode.key = value
		#search for childvalue and see if the node has children, if it doesnt then delete
		childNode = self.searchNode(value, self.rootnode)
		if childNode!=None :
			if childNode.leftChild == None and childNode.rightChild == None :
				#delete child node
				if childNode.parent.leftChild!=None and childNode.parent.leftChild.key == childNode.key :
					childNode.parent.leftChild = None				
				elif childNode.parent.rightChild!=None and childNode.parent.rightChild.key == childNode.key :
					childNode.parent.rightChild = None
				print "%s has been deleted"	%childNode.key
				childNode = None
			else:
				print "Node not deleted, has children"
		else:
			print "Node not found"
			
    def printTree(self,currentNode):
		#print all the nodes in pre-order traversal
		if currentNode != None:
			print currentNode.key
			self.printTree(currentNode.leftChild)
			self.printTree(currentNode.rightChild)
