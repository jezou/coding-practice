#implementing linked lists in python 

#singly linked list (using None as end of list)

class SinglyNode:
	def __init__(self, value, next):
		self.value = value
		self.next = next

class SinglyLinkedList:
	def __init__(self, head):
		self.head = head

	#insert value after node
	def insertAfter(node, value):
		temp = node.next
		node.next = SinglyNode(value, temp)

	#insert value at head of list
	def insertFirst(self, value):
		new_node = SinglyNode(value, self.head)
		self.head = new_node

	#delete value at head of list
	def deleteFirst(self):
		node = self.head
		self.head = node.next


	#return True if value in list (via ==) False if not
	def search(self, value):
		node = self.head
		while node:
			if node.value == value:
				return True
			node = node.next
		return False

	#traverse and print list		
	def traverse(self):
		print("Traversal:")
		node = self.head
		while node:
			print(node.value)
			node = node.next

	#reverse list
	def reverse(self):
		prev = None
		current = self.head
		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		#last node is head
		self.head = prev

#for testing
l = SinglyLinkedList(SinglyNode(5, None))
l.insertFirst(0)
l.insertFirst(1)
l.traverse()
print(l.search(-1))
print(l.search(5))
l.reverse()
l.traverse()
l.deleteFirst()
l.traverse()
