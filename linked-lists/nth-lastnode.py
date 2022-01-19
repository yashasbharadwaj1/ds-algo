class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def length(self):
        cur=self.head
        while cur:
            count=count+1
            cur=cur.next
        return count

    def print_nth_from_last(self,n):
       length=self.length()
       cur=self.head
       while cur:
           if n ==length:
               print(cur.data)
               return cur.data
           length=length-1
           cur=cur.next  
       if cur is None:
            return 
