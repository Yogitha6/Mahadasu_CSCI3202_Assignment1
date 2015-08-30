class StackImplementation:

    def __init__(self):
	    self.stack = []
		
    def push(self, element):
	    self.stack.append(element)
		
    def pop(self):
	    return self.stack.pop()

    def checkSize(self):
	    return len(self.stack)
