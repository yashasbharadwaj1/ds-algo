  def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        
        if (p == None and q != None) or (q == None and p != None):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)