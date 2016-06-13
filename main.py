import process_input
import converter

items = {}
units = {}
#Greetings to the user
print "\nWelcome to the Intergalactic Converter"

#Ask for input
user_input = raw_input("\nSo, What can I do for you today?\n\n")

while True:
	user_input_words = user_input.split()
	item_list = []
	error_response = ""
	type_of_input = process_input.get_type_of_input(user_input)
	if type_of_input == "Numeric Assignment":
		items[user_input_words[0]] = user_input_words[2]
		print "Ok, fine. I have memorize the item and its value !!"
	elif type_of_input ==  "Unit Assignment":
		unit_assignment_detail = process_input.get_unit_assignment_detail(user_input_words)
		credits = unit_assignment_detail['credits']
		unit_items = unit_assignment_detail['items']
		unit_items_length = len(unit_items)
		for item in unit_items:
			if item != unit_items[unit_items_length-1]:
				if item in items:
					item_list.append(item)
				else:
					error_response = "Sorry, there is no value assigned for \""+ item + "\" yet."
					break
			else:
				if item in items:
					error_response = "Unit can not be of same name as any of the items."
					break
				else:
					units[item] = 0
		if error_response != "":
			print error_response
		else:
			converted_result = converter.earth_to_galaxy_conversion(item_list, items)
			if str(converted_result).isdigit():
				units[item] = "{0:.2f}".format(float(credits)/float(converted_result))
				print "Thats cool. Unit has been saved in my memory !!"
			else:
				print converted_result
	elif type_of_input ==  "Question":
		unit_val = 0.00
		input_length = len(user_input)
		start = user_input.find('is') + 3
		substr = user_input[start:length-1]
		if "credits" in user_input.lower():
			for var in substr.split():
				if var != substr.split()[len(substr.split())-1]:
					if var in items:
						item_list.append(var)
					else:
						error_response = "Sorry, there is no value assigned for \""+ var + "\" yet."
						break
				else:
					if var in units:
						unit_val = units[var]
					else:
						error_response = "Sorry, there is no unit assigned for \""+ var + "\" yet."
						break
			if error_response != "":
				print error_response
			else:
				ret = conversion.variables_for_conversion(item_list, items)
				if str(ret).isdigit():
					output = ret * float(unit_val)
					print substr.strip() + " is " + str(output) + " Credits"
				else:
					print ret
		else:
			for var in substr.split():
				if var in items:
					item_list.append(var)
				else:
					error_response = "Sorry, there is no value assigned for \""+ var + "\" yet."
					break
			if error_response != "":
				print error_response
			else:
				ret = conversion.variables_for_conversion(item_list, items)
				if str(ret).isdigit():
					print substr.strip() + " is " + str(ret)
				else:
					print ret
	else:
		print type_of_input
	user_input = raw_input("\nWhat more I can do for you?\n")
