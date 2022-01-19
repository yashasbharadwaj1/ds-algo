class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def remove_duplicates(self):
      cur =self.head
      prev=None
      duplicate_dictionary=dict()
      while cur:
          if cur in duplicate_dictionary:
              prev.next=cur.next
              cur=None
          else:
              duplicate_dictionary[cur]=1
              prev=cur
      cur=prev.next