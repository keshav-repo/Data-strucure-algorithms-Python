### Linked List
1. A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
 ```
 class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 ```
File reference: LinkedListIntro.py

### Coding Question: 
1. Find the middle of a given linked list ? \
  Input:  1->2->3->4->5 \
  Output: 3 \
  Input 2: 1->2->3->4->5->6 \
  Output: 4 \
  References: [g4g](https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/) \
  Solution: MiddleInLinkedList.py 
2. Find nth node from the end of linked list
  Input:  1->2->3->4->5->6->7->8->9 , N = 2\
  Output: 8 \
  References: [g4g](https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1) \
  Solution: NnodeFromEnd.py
3.   

