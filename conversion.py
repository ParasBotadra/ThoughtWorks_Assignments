import re
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
	error = ""
	for var in var_list:
		result_string += str(variables[var])
	if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',result_string)!= None:
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
	else:
		error = "Hold On, It seems you are trying to convert invalid combination of symbols. Plese try again."
		return error
