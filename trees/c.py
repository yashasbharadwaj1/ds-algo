
from collections import deque 
from binary_tree import *
from binary_tree_node import * 
def level_order_traversal(root):
    if not root:
        print("None",end="")
    else:
        result=""
        queues=[deque(),deque()]
        current_queue=queues[0]
        next_queue = queues[1]
        current_queue.append(root)
        level_number = 0
        while current_queue:
            temp=current_queue.popleft()
            print(str(temp.data),end="")
            result+=str(temp.data)+""
            if temp.left:
                next_queue.append(temp.left)  
            if temp.right:
                next_queue.append(temp.right)
            if not current_queue:
                level_number+=1 
                if next_queue:
                    print(":",end="")
                current_queue=queues[level_number%2] 
                  
