#insertion at the end of the singlylinked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
ll=LinkedList()
ll.prepend('a')
ll.prepend('b')
ll.prepend('c') 
ll.printlist()   