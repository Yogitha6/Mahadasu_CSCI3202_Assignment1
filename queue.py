import Queue

class QueueImplementation:

   def __init__(self):
       'initializing a queue'
       self.queue = Queue.Queue()

   def enqueue(self, element):
       'adding element to the queue'
       self.queue.put(element)
	   
   def dequeue(self):
       'poping an element from the queue'
       return self.queue.get()

   def isEmpty(self):
       'returns true if the queue is empty'
       return self.queue.empty()
