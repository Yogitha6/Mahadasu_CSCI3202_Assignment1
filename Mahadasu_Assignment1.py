from queue import *
from stack import *
from binarytree import *
from graph import *

#Testing the queue
print "Testing the Queue Implementation:"
print "--------------------------------------------------------------"

#creating an instance of the class
queue = QueueImplementation()

#Initializing the queue
queue.__init__();

#Inserting elements into the queue
print "Adding the first 10 integers to the queue"
for i in range(1,11):
    queue.enqueue(i)

#Popping out the elements from the queue in First in First Out Order
print "Popping the elements out of the queue in FIFO order"
while queue.isEmpty()!=True:
    print(queue.dequeue())
print "--------------------------------------------------------------"

#Testing the stack
print "Testing the Stack Implementation:"
print "--------------------------------------------------------------"

#creating an instance of the stack
stack = StackImplementation()

#Initializing the stack
stack.__init__()

#Inserting elements into the stack
print "Adding the first 10 integers to the stack"
for i in range(1,11):
    stack.push(i)

#Popping out the elements from the stack in Last in First Out Order
print "Popping the elements out of the stack in LIFO order"
while stack.checkSize()!=0:
    print(stack.pop())

print "--------------------------------------------------------------"

#Testing the Binary tree
print "Testing the BinaryTree Implementation:"
print "--------------------------------------------------------------"

#creating an instance of the binary tree
tree = TreeImplementation()

#Initializing the tree
tree.__init__()

#Inserting elements into the tree
print "Adding the first 10 integers to the tree"
for i in range(0,11):
	tree.add(i,(i+1)/2 - 1)

#Printing the elements from the tree by preorder traversal
print "Printing the elements in the tree in preorder traversal"
tree.printTree(tree.rootnode)

#Deleting elements from the tree
print "Deleting 4 elements from the tree"
for i in range(7,11):
    tree.delete(i)
	
#Printing the elements from the tree by preorder traversal
print "Printing the elements in the tree in preorder traversal"
tree.printTree(tree.rootnode)
print "--------------------------------------------------------------"

#Testing the Graph
print "Testing the Graph Implementation:"
print "--------------------------------------------------------------"

#creating an instance of the graph
graph = GraphImplementation()

#Initializing the graph
graph.__init__()

#Adding vertices to the graph
print "Adding the first 10 integers to the graph"
for i in range(0,11):
    graph.addVertex(i)

#Adding edges to the graph
print "Adding the 20 edges to the graph"
for i in range(0,11):
	graph.addEdge(i, (i+1)/2 + 1)
	graph.addEdge(i, i/2)

#Finding 5 vertices in the graph
for i in range(4,10):
    graph.findVertex(i)
