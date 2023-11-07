

# About the part of list --------------------------------------------- 




# Creation of a list in using the interval [0, n]
list_created = [1, 'papa', 3, 29, 'good']


# Having a entier list, then put it into a string list
string_list = []
entier_list = [1, 2, 3, 4, 5, 6]
for each_element in entier_list:
	convert = str(each_element)
	string_list.append(convert)


# Putting a list with elements in lowercase into a list within which elements are in upper
upper_list = []
lower_list = ['a', 'b', 'c', 'd', 'e', 'f']
for each_element in lower_list:
	 upper_list.append(each_element.upper())
	 


# Creating a list with elements form another, but elements having their index divisiblle by 3
first_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
second_list = []
for x in range(0, len(first_list)):
	if (x%3 == 0):
		second_list.append(first_list[x])

print(second_list)



# Creating a list inside it all the 3 elements set up as a tuple...
first_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
the_other_list = []
list_test = []
var_test = 0
my_tuple = ()

buffer_list = []
for x in range(0, len(first_list)):
	
	if(var_test < 3):
		buffer_list.append(first_list[x])
		var_test +=1

	if len(buffer_list) == 3:
		my_tuple = tuple(buffer_list)
		the_other_list.append(my_tuple)
		del my_tuple
		buffer_list.clear()
		var_test = 0
	elif (len(buffer_list) < 3 and (x+1 == len(first_list))):
		if len(buffer_list) != 0:
			for each in buffer_list:
				the_other_list.append(each)
			
print(the_other_list)




# removing from a list all repeated elements...
list_in_single_elements = []
list_into_repeated_elements = [1, 3, 67, 1, 12, 'ESIH', [40], 1, 'ESIH']

for element in list_into_repeated_elements:
	if element not in list_in_single_elements:
		list_in_single_elements.append(element)
	else:
		continue

print(list_in_single_elements)


# Getting a list in using all common elements from two lists........
list_one = ['python', 'love', 'ESIH', 'life', 'code', 'music', 'prayer', 'God', 'poetry', 'family', 'friend', 'nothing']
list_two = ['python', 'ESIH', 'code', 'music', 'prayer', 'God', 'family', 'friend', 'nothing']
list_in_resume = []
for elm in list_one:
	if elm in list_two:
		list_in_resume.append(elm)
	else:
		continue

print(list_in_resume)




# Getting a list in using all distinguished elements from two lists........
list_first = ['python', 'love', 'ESIH', 'life', 'code', 'music', 'prayer', 'God', 'poetry', 'family', 'friend', 'nothing']
list_second = ['python', 'ESIH', 'code', 'music', 'prayer', 'God', 'family', 'friend', 'nothing']
list_third = []
for elm in list_first:
	if elm not in list_second:
		list_third.append(elm)
	else:
		continue
for elm in list_second:
	if elm not in list_second:
		list_third.append(elm)
	else:
		continue

print(list_third)




# from a dictionary, grt two lists... 
the_dict = {"key1":"python", "key2":"Java", "Key3":"linux", "key4":"light"}
my_list_in_values = []
my_list_in_keys = list(the_dict.keys())
for keyy in my_list_in_keys:
	my_list_in_values.append(the_dict[keyy])

print(my_list_in_keys)
print(my_list_in_values)




# Union of three lists in one... 
list_first = ['python', 'love', 'ESIH', 'life', 'code', 'music', 'prayer', 'God', 'poetry', 'family', 'friend', 'nothing']
list_second = ['python', 'enjoy', 'live', 'music', 'network', 'God', 'math', 'friend', '777']
list_third = ['python', 'road', 'sin', 'life', 'code', 'music', 'run', 'God', 'data', 'family', 'friend', 'LOLLLLLLLL']
list_in_the_end = []

for el_1 in list_first:
	if ((el_1 not in list_second) and (el_1 not in list_third)):
		list_in_the_end.append(el_1)
for el_1 in list_second:
	if ((el_1 not in list_first) and (el_1 not in list_third)):
		list_in_the_end.append(el_1)
for el_1 in list_third:
	if ((el_1 not in list_second) and (el_1 not in list_first)):
		list_in_the_end.append(el_1)

print(list_in_the_end)












print(lower_list)
print(upper_list)









































