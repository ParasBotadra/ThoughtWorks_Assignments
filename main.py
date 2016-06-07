import process_input
import process_unit_assignment
import conversion

variables = {}
units = {}
#Greetings to the user
print "\nWelcome to the Intergalactic Converter"

#Ask for input
user_input = raw_input("\nSo, What can I do for you today?\n\n")

while True:
	words = user_input.split()
	var_list = []
	error_response = ""
	"""
	Processable input can of three major types:
	1. Numeric Assignment
	2. Unit Assignment to the Numeric Value
	3. Question for conversion, it can be either earth to galaxy or galaxy to earth  
	"""
	type_of_input = process_input.process_input(user_input)
	if type_of_input == "Numeric Assignment":
		variables[words[0]] = words[2]
		print "Ok, fine..!!"
	elif type_of_input ==  "Unit Assignment":
		#glob glob Silver is 34 Credits
		get_input = process_unit_assignment.process_unit_assignment(words)
		credits = get_input['credits']
		unit_vars = get_input['vars']
		unit_vars_length = len(unit_vars)
		for var in unit_vars:
			if var != unit_vars[unit_vars_length-1]:
				if var in variables:
					var_list.append(var)
				else:
					error_response = "Sorry, there is no value assigned for \""+ var + "\" yet."
					break
			else:
				if var in variables:
					error_response = "Unit can not be of same name as any of the variables."
					break
				else:
					units[var] = 0
		if error_response != "":
			print error_response
		else:
			ret = conversion.variables_for_conversion(var_list, variables)
			if str(ret).isdigit():
				units[var] = "{0:.2f}".format(float(credits)/float(ret))
				print "Thats cool !!"
			else:
				print ret
	elif type_of_input ==  "Question":
		#how much is pish tegj glob glob ?
		#how many Credits is glob prok Silver ?
		get_input = process_unit_assignment.process_question(user_input)
		if get_input['credits']:
			pass
		else:
			length = len(user_input)
			ret = conversion.variables_for_conversion(get_input['vars'], variables)
			start = user_input.find('is') + 3
			substr = user_input[start:length-1]
			if str(ret).isdigit():
				print substr.strip() + " is " + str(ret)
			else:
				print ret
	else:
		print type_of_input
	user_input = raw_input("\nWhat more I can do for you?\n")
