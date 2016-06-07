def process_unit_assignment(words):
	var = []
	i = 0
	while words[i] != "is":
		var.append(words[i])
		i += 1
	credits = words[i+1]
	return {'vars' : var, 'credits' : credits}


def process_question(user_input):
	var = []
	user_input.replace("?","")
	length = len(user_input)
	if "credits" in user_input.lower():
		start = user_input.find('is') + 3
		substr = user_input[start:length-1]
		var = substr.split()
		return {'vars' : var, 'credits' : True}
	else:
		start = user_input.find('is') + 3
		substr = user_input[start:length-1]
		var = substr.split()
		return {'vars' : var, 'credits' : False}
