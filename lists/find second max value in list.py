#find second max value in list.py
#sol 1
def find_second_maximum_sol_1(lst):
	first_max =float('-inf')
	second_max =float('-inf')
	for item in lst:
		if item > first_max:
			first_max = item 
	# find max relative to first max 
	for item in lst:
		if item != first_max and item > second_max:
			second_max = item 
	return second_max




print(find_second_maximum_sol_1([9,2,3,6]))