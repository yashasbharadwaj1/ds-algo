#write a python program to check whether a given key already exists in a dictionary
d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
	if x in d:
		print('key exists in dictionary')
    else:
    	print('key does not exist in dictionary')
    is_key_present(5)
    is_key_present(9)