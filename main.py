import process_input

variables = {}
values = {'I' : 1,
		  'V' : 5,
		  'X' : 10,
		  'L' : 50,
		  'C' : 100,
		  'D' : 500,
		  'M' : 1000}
#Greetings to the user
print "\nWelcome to the Intergalactic Converter"

#Ask for input
user_input = raw_input("\nSo, What can I do for you today?\n\n")

while True:
	words = user_input.split()
	"""
	Processable input can of three major types:
	1. Numeric Assignment
	2. Unit Assignment to the Numeric Value
	3. Question for conversion, it can be either earth to galaxy or galaxy to earth  
	"""
	type_of_input = process_input.process_input(user_input)
	if type_of_input == "Numeric Assignment":
		variables[words[0]] = values[words[2]]
		print variables
	elif type_of_input ==  "Unit Assignment":
		print type_of_input
	else:
		print type_of_input
	user_input = raw_input("\nWhat next?\n")
