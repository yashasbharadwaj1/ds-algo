
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def levelOrder(self, root):
        if not root:
            return []
        stack = [(root,)]
        result = []
        while stack:
            current_lvl = []
            next_lvl = []
            nodes = stack.pop()
            for node in nodes:
                current_lvl.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            if next_lvl:
                stack.append(next_lvl)
            if current_lvl:
                result.append(current_lvl)
        return result          




         
