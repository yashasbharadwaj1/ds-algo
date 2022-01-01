    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        visited = {}
        ans = []
        while len(stack):
            curr = stack[-1]
            while curr.left and curr.left not in visited:
                curr = curr.left
                stack.append(curr)
            ans.append(curr.val)
            visited[curr] = True
            stack.pop()
            if curr.right and  curr.right not in visited:
                curr = curr.right
                stack.append(curr)
        return ans
        
