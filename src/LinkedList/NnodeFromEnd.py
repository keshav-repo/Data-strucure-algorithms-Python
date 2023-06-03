# 1->2->3->4->5->6->7->8->9, N=2
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "data {}".format(self.data)

head = Node(1)
root = head
for data in range(2, 10):
    node = Node(data)
    root.next = node
    root = node

root = head
while root != None:
    print(root.data, end=",")
    root = root.next
print("")

curr = head
count = 1
N = 3

while( count != N ):
    curr = curr.next
    count = count +1

print(curr.data)
nthNode = head

while(curr.next != None):
    curr = curr.next
    nthNode = nthNode.next

print("{} th node from last is {}".format(N, nthNode.data))
