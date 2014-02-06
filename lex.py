
import re
import StringIO
from collections import defaultdict

class Lexer(object):
	_ELEMENT = "ELEMENT"
	_PIN = "PIN"
	_ATTRIBUTE = "ATTRIBUTE"
	_VALUE = "VALUE"
	_CELL_START_PATTERN = '(.SUBCKT.*)'
	_CELL_END_PATTERN = '(^.ends)'
	_TRANSISTOR_PATTERN = '(^[X|m|M][0-9a-zA-Z_]+)'
	_RESISTOR_PATTERN = '(^[r|R][0-9a-zA-Z_]+)'
	_CAPACITOR_PATTERN = '(^[c|C][0-9a-zA-Z_]+)'
	_DIODE_PATTERN = '(^[d|D][0-9a-zA-Z_]+)'
	_ELEMENT_PATTERN = '(^[a-zA-z]+[a-zA-Z0-9]*)'
	_ATTRIBUTE_PATTERN = r'[\w_]+\s*=\s*[\w\.\-]+' 
	_PIN_PATTERN = r'\w+\s*:?\s*\w*'
	_VALUE_PATTERN = '(^[0-9eu.+-]+)'
	_VALUE_PATTERN_2 = '(=\w*.?\w*-?\w*)'
	_NEW_LINE_PATTERN = '(^[+ ]+)'
	_NAME_PATTERN = r'\w*\s*_?\s*\w*'
	def _merge_two_string(self, s1, s2):
		s2 = s1 + ' ' + s2
		return s2
	def _clean_string(self, s):
		s = s.lstrip("+ ")
		return s
	def _string_to_list(self, s):
		l = []
		stack = []
		s = s.replace('\n','')
		s = s.replace('\r','')
		l = s.split(" ")
		return l
	def _parse_one_line(self, s):
		d = {}
		i = 0
		ll = []
		line_2 = ""
		buf = StringIO.StringIO(s)
		while True:
			line = buf.readline()
			if line:
				if line.startswith('+'):
					line = self._clean_string(line)
					line_2 = self._clean_string(line_2)
					line = self._merge_two_string(line_2, line)
					line_2 = line
					continue
				ll = self._check_element(line_2)
				d[i] = ll
				i = i + 1
				line_2 = line
			else:
				ll = self._check_element(line_2)
				d[i] = ll
				i = i + 1
				return d
	def _is_attribute(self, s):
		a = re.match(self._ATTRIBUTE_PATTERN, s)
		if a:
			return True
		else:
			return False
	def _is_element(self, s):
		a = re.match(self._ELEMENT_PATTERN, s)
		if a:
			return True
		else:
			return False
	def _is_pin(self, s):
		a = re.match(self._PIN_PATTERN, s)
		e = re.match('([^=]+=[^=]+)', s)
		if a and e is None:
			return True
		else:
			return False
	def _is_value(self, s):
		a = re.match(self._VALUE_PATTERN, s)
		e = re.match('([^=]+=[^=]+)', s)
		if a and e is None:
			return True
		else:
			return False
	def _is_new_line(self, s):
		a = re.match(self._NEW_LINE_PATTERN, s)
		if a:
			return True
		else:
			return False
	def _is_cell(self, s):
		a = re.match(self._CELL_START_PATTERN, s)
		if a:
			return True
		else:
			return False
	def _tokenize_attribute(self, l):
		ll = []
		s = ''.join(l)
		n = re.match(self._NAME_PATTERN, s)
		v = re.search(self._VALUE_PATTERN_2, s)
		ns = n.group()
		vs = v.group()
		if n != 0 and v != 0:
			vs = vs.lstrip("= ")
			ll.append(ns)
			ll.append(vs)
		return ll
	def _check_element(self, s):
		ll = []
		t = re.match(self._TRANSISTOR_PATTERN, s)
		r = re.match(self._RESISTOR_PATTERN, s)
		c = re.match(self._CAPACITOR_PATTERN, s)
		d = re.match(self._DIODE_PATTERN, s)
		n = re.match(self._NEW_LINE_PATTERN, s)
		cc = re.match(self._CELL_START_PATTERN, s)
		ce = re.match(self._CELL_END_PATTERN, s)
		if t == 0 and r == 0 and c == 0 and d == 0 and n == 0 and cc == 0:
			return "Unrecognizable instructions"
		else:
			if t:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
		#		print ll
				return ll
			#	return "TRANSISTOR"
			if r:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
		#		print ll
				#print l[0].split()
				return ll
			#	return "RESISTOR"
			if c:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
		#		print ll
				return ll
			#	return "CAPACITOR"
			if d:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
		#		print ll
				return ll
			#	return "DIODE"
			if n:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
		#		print ll
				return ll
			#	return "NEW LINE"
			if cc:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			if ce:
				return
	def _make_tokens(self, l):
		ll = []
		for i in xrange(len(l)):
			ba = self._is_attribute(l[i])
			be = self._is_element(l[i])
			bp = self._is_pin(l[i])
			bv = self._is_value(l[i])
			bn = self._is_new_line(l[i])
			if ba:
				self._tokenize_attribute(l[i])
				ll = self._tokenize_attribute(l[i])
				lll = [self._ATTRIBUTE, ll]
			#	print lll
				ll.append(lll)
			if be and i == 0:
				lll = [self._ELEMENT, l[i]]
			#	print lll
				ll.append(lll)
			if bp and i != 0:
				lll = [self._PIN, l[i]]
			#	print lll
				ll.append(lll)
			if bv:
				lll = [self._VALUE, l[i]]
			#	print lll
				ll.append(lll)
		if not ll:
			return None
		else:
			return ll



