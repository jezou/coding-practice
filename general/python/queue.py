#implementations of queues in python

#array implementation
class ArrayQueue:
	def __init__(self,size):
		self.array = [None] * size
		self.front = 0
		self.back = 0
		self.maxSize = size
		self.currentSize = 0

	def isEmpty(self):
		return self.currentSize == 0

	def isFull(self):
		return self.currentSize == self.maxSize

	def enqueue(self, item):
		if self.isFull():
			print("Queue is full - could not enqueue")
		else:
			self.array[self.back] = item
			self.back = (self.back + 1) % self.maxSize
			self.currentSize += 1

	def dequeue(self):
		if self.isEmpty():
			print("Queue is empty - could not dequeue")
			return None
		else:
			item = self.array[self.front]
			self.front = (self.front + 1) % self.maxSize
			self.currentSize -= 1
			return item

#ArrayQueue Testing
'''
q = ArrayQueue(5)
q.enqueue(3)
q.enqueue(5)
q.enqueue(6)
q.enqueue(2)
q.enqueue(1)
#full
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
#empty
print(q.dequeue())
'''

#linked list implementation of queue

class QNode:
	def __init__(self, value, next):
		self.value = value
		self.next = next

class LinkedListQueue:
	def __init__(self):
		self.head = None
		self.back = None

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def enqueue(self, value):
		node = QNode(value, None)
		if self.isEmpty():
			self.head = node
			self.rear = node
		else: 
			self.rear.next = node
			self.rear = node

	def dequeue(self):
		if self.isEmpty():
			print("Queue is empty - could not dequeue")
			return None
		else:
			node = self.head
			self.head = self.head.next
			#for clarity, although self.rear is reset in enqueue if necessary
			if self.head is None:
				self.rear = None

			return node.value

#LinkedListQueue Testing
'''
q = LinkedListQueue()
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
q.enqueue(2)
q.enqueue(1)
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
'''






