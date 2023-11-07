


#   -------------------------------- About the STR ----------------------------------------------------------------------------------------------

# Consider a string............
the_variable = "the String in uSing by all HAITIAN diva"



# Put in lower...
string_in_lower = the_variable.lower()


print("\n")
# Displaying a list containing all pieces of a string splited in using "SPACE" as symbol cuting              
for each in the_variable.split(" ") :                         
	print(each, end=" ")
print("\n------------------------------------------------------------------------")


# Displaying all first letters in upper, but it's not as title mode...
right_string = ""
for each in the_variable.split(" ") : 
	val_ = each[0]
	vala_ = each[0].upper()
	varReplace = each.replace(val_, vala_, -1)           # -1    to make a all replace
	right_string += varReplace + " " 

print(right_string)


# Get another string with each first letter from each letter from the a string splited 
string_with_each_first_letter = ""
for each in the_variable.split(" ") : 
	first = each[0]
	string_with_each_first_letter += first
print("\n")
print(string_with_each_first_letter)



# replace each  'a'  by   '@'
string_treated = ""
if "a" in the_variable:
	string_treated = the_variable.replace("a", "@", -1)
	
print(string_treated)
		
	


# Putting in inverse mode ------------------------
string_lengh = len(the_variable)
i = 1
string_inverted = ""
for x in range(0, string_lengh):
	string_inverted += the_variable[string_lengh - i]
	i += 1

string_inverted_in_upper = string_inverted.upper()




# Displaying the index of the first "a" as charactere
index_value = -1
for the_first_a in the_variable:
	if the_first_a == "a":
		index_value = the_variable.index(the_first_a)
		break
	else:
		continue

print("\n")
print(index_value)
	


# Displaying the total index of all "a" as charactere

total_index = 0
for i in range(0, len(the_variable)):
	if the_variable[i] == "a" or the_variable[i] == "A":
		total_index += i
	else:
		continue

print("\n")
print(total_index)





# list of index  any 'a'
list_index = []
for i in range(0, len(the_variable)):
	if the_variable[i] == "a":
		list_index.append(i)
	else:
		continue

print(list_index)



# Remove all spaces from a string...
string_without_spaces = ""
for letter in the_variable:
	if letter.isspace():
		continue
	else:
		string_without_spaces += letter

print(string_without_spaces)





