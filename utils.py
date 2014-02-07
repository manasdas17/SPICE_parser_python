

def merge_two_string(s1, s2):
	s2 = s1 + ' ' + s2
	return s2

def clean_string(s):
	s = s.lstrip("+ ")
	return s

def string_to_list(s):
	l = []
	stack = []
	s = s.replace('\n','')
	s = s.replace('\r','')
	l = s.split(" ")
	return l

def format_input_string(s):
	l = s.split(' ')
	for i in xrange(len(l)):
		l[i] = ['PIN', l[i]]
	return l
