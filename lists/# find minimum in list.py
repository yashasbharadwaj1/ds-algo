# find minimum in list
def find_minimum(lst):
	if(len(lst)<=0):
		return None
	minimum = lst[0]
	for ele in lst:
		if ele < minimum:
			minimum = ele 
	return minimum 
print(find_minimum([9,2,3,6]))