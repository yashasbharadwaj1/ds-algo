#O(n square)

def find_product(lst):
	result=[]
	left=1
	for i in range(len(lst)):
		currentproduct=1
	    for ele in lst[i+1:]:
	    	currentproduct = currentproduct *ele 
	    result.append(currentproduct*left)
	    left = left * lst[i]
	return result 
print(find_product([1,2,3,4]))


