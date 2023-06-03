# 1->2->3->4->5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

fast = head
slow = head

while( slow != None and fast != None and fast.next != None):
    slow = slow.next
    fast = fast.next
    fast = fast.next

print(slow.data)
