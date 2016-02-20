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

#for testing
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




