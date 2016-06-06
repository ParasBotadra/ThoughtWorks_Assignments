def process_unit_assignment(words):
	var = []
	i = 0
	while words[i] != "is":
		var.append(words[i])
		i += 1
	credits = words[i+1]
	return {'vars' : var, 'credits' : credits}
