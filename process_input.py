def get_type_of_input(user_input):
	"""
	It processes the input and recognize the type of user input.
	Processable input can of three major types:
	1. Numeric Assignment
		i. input should have only three words
		ii. it should not end with '?'
		iii. second word should be 'is'
		iv. third word should be either of 'I,V,X,L,C,D,M'
	2. Unit Assignment to the Numeric Value
		i. input should have more than three words
		ii. last word should be "Credits"
		iii. second last word should be any digit
		iv. third last word should be 'is'
	3. Question for conversion, it can be either earth to galaxy or galaxy to earth
		i. input should have more than three words
		ii. input should start with either "how much" or "hoe many"
		iii. it should ends with '?'
		iv. it should contains "is" keyword
	"""
	words = user_input.split()
	input_length = len(words)
	if input_length == 3 and words[input_length-2].lower() == 'is':
		if len(words[input_length-1]) == 1 and words[input_length-1] in ('I','V','X','L','C','D','M'):
			return ("Numeric Assignment")
		else:
			return ("Sorry, but there is no such symbol used in the galaxy as \""+ words[input_length-1] +"\".\nPlease use any symbol from the below list:\nI\nV\nX\nL\nC\nD\nM")
	elif input_length > 3 and words[input_length-1].lower() == 'credits' and words[input_length-2].isdigit() == True and words[input_length-3].lower() == 'is' :
		return ("Unit Assignment")
	elif input_length > 3 and words[0].lower() == 'how' and words[1].lower() in ('many','much') and "?" == user_input[len(user_input)-1] and "is" in user_input.lower():
		return ("Question")
	else:
		return ("I have no idea what you are talking about")

def get_unit_assignment_detail(words):
	items = []
	i = 0
	while words[i] != "is":
		items.append(words[i])
		i += 1
	credits = items[i+1]
	return {'items' : items, 'credits' : credits}
