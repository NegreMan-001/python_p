


# from a dictionary, get a list (containing all the values)... 
the_dict = {"key1":"python", "key2":"Java", "Key3":"linux", "key4":"light"}
my_list_in_values = []

for keyy in the_dict.keys():
	my_list_in_values.append(the_dict[keyy])

print(my_list_in_values)






# verification if the '{' forward and/or backward
user_entry = input("Enter something as expected      ")
if user_entry.startswith("{") and user_entry.endswith("}"):
	print("The content is really encompassed with {} ")
else:
	print("It's not encompased... ")






# Running a whole dictionary through, then display all keys...
interation = 0
for this_key, its_value in the_dict.items():
	interation +=1
	print(" The {0} is nothing else than --------> {1} \n".format(interation, this_key))





# Running a whole dictionary through, then display all values...
interation = 0
for this_key, its_value in the_dict.items():
	interation +=1
	print(" The {0} is nothing else than --------> {1} \n".format(interation, its_value))




# Making a copy of a existing dictionary....
#newer_dict = the_dict.copy()      
new_dict = {}
for e_key in the_dict:
	new_dict.update({e_key:the_dict[e_key]})

print(new_dict)




# Inside the dictionary, if the type a value-content is str, surround it with '_'
for t_key in the_dict.keys():
	if isinstance (the_dict[t_key], str):
		the_dict[t_key] = "_{0}_".format(its_value)

print(the_dict)



# Creating a dictionary with values of keys which are digit from another one... 
other_dict = {"a":"10", "b":"17Y", "c":"Raul", "d":"1804"}
dict_dict = {}
for t_key in other_dict.keys():
	if isinstance (other_dict[t_key], str):
		if other_dict[t_key].isdigit():
			dict_dict.update({t_key:other_dict[t_key]})
		
print(dict_dict)



# Changing a dictionary into a list in which each key and its value make a tuple...
v_dict = {"a":"10", "b":"17Y", "c":"Raul", "d": 1804}
list_result = []
for key_k, value_k in v_dict.items():
	t_tuple = (key_k, value_k)
	list_result.append(tuple(t_tuple))

print(list_result)




# Changing a list_tuple into a dictionary...
list_tuple = [("a","10"), ("b","17Y"), ("c","Raul"), ("d", 1804)]
dict_t = {}
for eleme in list_tuple:
	dict_t.update({eleme[0]:eleme[1]})

print(dict_t)



# Joining two dictionaries to get a last one, in using some conditions... 
first_dict = {"a": 10, "b":"17Y", "c":"Raul", "d": [1804, 'code'], 8:{"ESIH"}}
second_dict = {"a": 102, "b":"17Y", "c":"Raul", "d": 1804, "e":("good", "november")}
end_dict = {}

for element_f in first_dict.keys():
	if element_f not in second_dict.keys():
		end_dict.update({element_f:first_dict[element_f]})
	else:
		if ((isinstance(first_dict[element_f], int)) and (isinstance(second_dict[element_f], int))):
			var_add = first_dict[element_f] + second_dict[element_f]
			end_dict.update({element_f:var_add})
		elif ((isinstance(first_dict[element_f], str) or isinstance(first_dict[element_f], list) or isinstance(first_dict[element_f], set)) and  
		(isinstance(second_dict[element_f], str) or isinstance(second_dict[element_f], list) or isinstance(second_dict[element_f], set))):
			val_conca = first_dict[element_f] + second_dict[element_f]
			end_dict.update({element_f:val_conca})
		else:
			continue
for e in second_dict.keys():
	if (e not in end_dict.keys()) and (e not in first_dict.keys()):
		end_dict.update({e:second_dict[e]})
	else:
		continue

print(end_dict)





















