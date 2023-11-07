
#   Function -----------------------------------------------------------------------



# function ask as parameter a word, then it return the reverse of this one...

def inversing_function(para_word = "nothing"):
	newer_string = ""
	if isinstance(para_word, str):
		v_l = len(para_word)
		for i in range(0, v_l):
			newer_string +=para_word[v_l - (i + 1)]
		return newer_string
	else:
		print("\t You entered a bad thing...")
		return newer_string

# calling 
print(inversing_function())
print(inversing_function(123))
print(inversing_function("Good morning"))







# Function generating a code with n characters alphabetic...
import random
def function_generate_code_with_n_alph():
	code_generated = ""
	lengh_code = random.choice([15, 21, 17, 7])
	for each in  range(0, lengh_code):
		numeric = random.randint(0, 9)
		alphabet = random.choice(['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
		if each%4 == 0:
			code_generated += alphabet
		elif each%4 == 1:
			code_generated += alphabet
		elif each%4 == 2:
			code_generated += str(numeric)
		elif each%4 == 3:
			code_generated += alphabet
	print(code_generated)	
	
# calling
function_generate_code_with_n_alph()





# Function generating a code with n characters alphabetic without repeating... 
import random
def function_generate_code_with_n_alph_no_repeat():
	code_generated = ""
	lengh_code = random.choice([15, 21, 17, 7])
	for each in  range(0, lengh_code):
		alphabet = random.choice(['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
		if each%4 == 0:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
		elif each%4 == 1:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
		elif each%4 == 2:
			if alphabet not in code_generated:
				new_val = alphabet.upper()
				if new_val not in code_generated:
					code_generated += alphabet.upper()
				else:
					continue
			else:
				continue
		elif each%4 == 3:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
	print(code_generated)	
	
# calling
function_generate_code_with_n_alph_no_repeat()









# Function generating a code with n characters alphabetic_numeric without repeating... 
import random
def function_generate_code_with_n_alph_numeric_no_repeat():
	code_generated = ""
	lengh_code = random.choice([15, 21, 17, 7])
	for each in  range(0, lengh_code):
		numeric = random.randint(0, 9)
		alphabet = random.choice(['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
		if each%4 == 0:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
		elif each%4 == 1:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
		elif each%4 == 2:
			num_str = str(numeric)
			if num_str not in code_generated:
				code_generated += num_str
			else:
				continue
		elif each%4 == 3:
			if alphabet not in code_generated:
				code_generated += alphabet
			else:
				continue
	print(code_generated)	
	
# calling
function_generate_code_with_n_alph_numeric_no_repeat()






# Having a list in string format, generate a SLUG from the string...
import string 
def slug_function():
	new_string = ""
	list_with_one_string = ['jean Daniel/\/_) 9 oiur-1-PPPP ']
	in_str = str(list_with_one_string)
	for x in range(0, len(in_str)):
		if in_str[x] in string.ascii_lowercase:
			new_string += in_str[x]
		elif in_str[x].isspace() or in_str[x] == "-" or in_str[x] == "_":
			new_string += "-"
		elif in_str[x].isdigit():
			new_string += in_str[x]
		else:
			continue

	print(new_string)
	

# calling 
slug_function()





# Function in which each letter of the word as parameter is separated from others by comma
def my_function_separator(the_word ="Nothing was passed"):
	new_comma_word = ""
	for each in the_word:
		new_comma_word += each
		if the_word.index(each) < (len(the_word) - 1):
			new_comma_word +=","
	
			

	print(new_comma_word)

# calling 
my_function_separator()





# scripting function
def script_funct(my_word = "Daniel"):
	script = ""
	for v in my_word:
		script += str(my_word.index(v))
	
	
	print(script)

#calling
script_funct()






# function for decripting... 
import string 
def my_function_inverse_script(param = "0-11-14"):
	result = ""
	parameter = param.split("-")
	alpha = string.ascii_lowercase
	for val in parameter:
		if val.isdigit():
			result += alpha[int(val)]
		else:
			continue

	print(result)
	
#calling... 
my_function_inverse_script()





# funcion taking two parameters and returns in tuple both values permitted
def change_function(val = "First", val1 = "Second"):
	var_buf = val
	val = val1
	val1 = var_buf
	ret = tuple((val, val1))
	
	return ret


#calling...
print(change_function())






# function that takes a name and... 
def name_function(name = "Jean-Daniel Florestal"):
	final_value = ""
	t = "-"
	name_cor = ""
	if t in name:
		name_cor = name.replace("-", " ")
	else:
		name_cor = name
	name_split = name_cor.split()
	
	for each in name_split:
		final_value += each[0]
	
	print(final_value)


name_function()



















