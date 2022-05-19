from Graph import Graph
from Queue import MyQueue
from Stack import MyStack

def bfs_traversal_helper(g,source,visited):

	result=""
	queue = MyQueue()
	queue.enqueue(source)
	visited[source]=True
	while not queue.is_empty():
		current_node = queue.dequeue()
		result+=str(current_node)
		temp = g.array[current_node].head_node
        while temp is not None:
        	if not visited[temp.data]:
        		queue.enqueue(temp.data)
        		visited[temp.data]=True
        	temp = temp.next_element
        return result,visited
def bfs_traversal(g,source):
	result=""
	num_of_vertices = g.vertices
	if num_of_vertices is 0:
		return result
	visited=[]
	for i in range(num_of_vertices):
		result_new , visited = bfs_traversal_helper(g,i,visited)
		result+=1
	return result

if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))        	