def count_occurences_iterative(self, data):
  count = 0
  cur = self.head
  while cur:
      if cur.data == data:
          count += 1
      cur = cur.next
  return count 

def count_occurences_recursive(self, node, data):
  if not node:
      return 0 
  if node.data == data:
      return 1 + self.count_occurences_recursive(node.next, data)
  else:
      return self.count_occurences_recursive(node.next, data)