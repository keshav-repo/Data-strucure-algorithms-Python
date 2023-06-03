# node with data and next as None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "data {}".format(self.data)

# initialising the linked list root node
root = Node(1)
head = root

# adding a element and link with root node
node = Node(2)
root.next = node
root = node

node = Node(3)
root.next = node
root = node

node = Node(4)
root.next = node
root = node

# print all the nodes from head
head_cpy = head
while( head_cpy != None):
    print(head_cpy.data, end="->")
    head_cpy = head_cpy.next
print("")

# delete first element from the node
temp = head
head = head.next
del temp
head_cpy = head
while( head_cpy != None):
    print(head_cpy.data, end="->")
    head_cpy = head_cpy.next
