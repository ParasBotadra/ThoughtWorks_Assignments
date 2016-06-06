#import re

def process_input(user_input):
	"""
	Checks the type of user input
	1. Numeric assignment clause:
		i. input should have only three words
		ii. it should not end with '?'
		iii. second word should be 'is'
		iv. third word should be either of 'I,V,X,L,C,D,M'
	"""
	#count = len(re.findall(r'\w+', user_input))
	words = user_input.split()
	length = len(words)
	if length == 3 and words[length-2].lower() == 'is':
		if len(words[length-1]) == 1 and words[length-1] in ('I','V','X','L','C','D','M'):
			return ("Numeric Assignment")
		else:
			return ("Sorry, but there is no such symbol used in the galaxy as \""+ words[length-1] +"\".\nPlease use any symbol from the below list:\nI\nV\nX\nL\nC\nD\nM")
	elif length > 3 and words[length-1].lower() == 'credits' and words[length-2].isdigit() == True and words[length-3].lower() == 'is' :
		return ("Unit Assignment")
	elif length > 3 and words[length-length].lower() == 'how' and words[length-(length-1)].lower() in ('many','much') and "?" == user_input[len(user_input)-1] and "is" in user_input.lower():
		return ("Question")
	else:
		return ("I have no idea what you are talking about")
