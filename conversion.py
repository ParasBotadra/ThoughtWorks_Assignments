values = {'I' : 1,
		  'V' : 5,
		  'X' : 10,
		  'L' : 50,
		  'C' : 100,
		  'D' : 500,
		  'M' : 1000}

def variables_for_conversion(var_list, variables):
	result_string = ""
	i = 0
	total = 0
	for var in var_list:
		result_string += str(variables[var])
	str_result = len(result_string)
	while i <= str_result-1:
		if i != str_result - 1:
			if values[result_string[i]] < values[result_string[i+1]]:
				total = total + (values[result_string[i+1]] - values[result_string[i]])
				i = i+2
			else:
				total = total + values[result_string[i]]
				i = i+1
		else:
			total = total + values[result_string[i]]
			i = i+1
	return total
