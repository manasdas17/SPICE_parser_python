
import re
import StringIO
from collections import defaultdict

class Lexer(object):
	_ELEMENT = "ELEMENT"
	_PIN = "PIN"
	_ATTRIBUTE = "ATTRIBUTE"
	_VALUE = "VALUE"
	_TRANSISTOR_PATTERN = '(^[X|m|M][0-9a-zA-Z_]+)'
	_RESISTOR_PATTERN = '(^[r|R][0-9a-zA-Z_]+)'
	_CAPACITOR_PATTERN = '(^[c|C][0-9a-zA-Z_]+)'
	_DIODE_PATTERN = '(^[d|D][0-9a-zA-Z_]+)'
	_ELEMENT_PATTERN = '(^[a-zA-z]+[a-zA-Z0-9]*)'
#	_PIN_PATTERN = '(^[a-zA-z]+[0-9]*[:]?[a-zA-Z0-9]*)'
#	_ATTRIBUTE_PATTERN = '(^[a-zA-Z0-9_]+[0-9]*(\s)*[=](\s)*[a-z0-9.-]+)'
	_ATTRIBUTE_PATTERN = r'[\w_]+\s*=\s*[\w\.\-]+' 
	_PIN_PATTERN = r'\w+\s*:?\s*\w+'
	_VALUE_PATTERN = '(^[0-9eu.+-]+)'
	_NEW_LINE_PATTERN = '(^[+ ]+)'
	def _string_to_list(self, s):
		l = []
		s = s.replace('\n','')
		s = s.replace('\r','')
		l = s.split(" ")
		return l
	def _parse_one_line(self, s):
		d = {}
		i = 0
	#	l = []
		ll = []
		buf = StringIO.StringIO(s)
		line = buf.readline()
		ll = self._check_element(line)
		d[i] = ll
	#	l.append(ll)
		while line:
			line = buf.readline()
			ll = self._check_element(line)
		#	l.append(ll)
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
		if a:
			return True
		else:
			return False
	def _check_element(self, s):
		ll = []
	#	ss = s
		t = re.match(self._TRANSISTOR_PATTERN, s)
		r = re.match(self._RESISTOR_PATTERN, s)
		c = re.match(self._CAPACITOR_PATTERN, s)
		d = re.match(self._DIODE_PATTERN, s)
		n = re.match(self._NEW_LINE_PATTERN, s)
		if t == 0 and r == 0 and c == 0 and d == 0 and n == 0:
			return "Unrecognizable instructions"
		else:
			if t:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			#	return "TRANSISTOR"
			if r:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				#print l[0].split()
				return ll
			#	return "RESISTOR"
			if c:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			#	return "CAPACITOR"
			if d:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			#	return "DIODE"
			if n:
				l = self._string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			#	return "NEW LINE"
	def _make_tokens(self, l):
		ll = []
		for i in xrange(len(l)):
			ba = self._is_attribute(l[i])
			be = self._is_element(l[i])
			bp = self._is_pin(l[i])
			bv = self._is_value(l[i])
			if ba:
				t = (self._ATTRIBUTE, l[i])
				print t
				ll.append(t)
			if be and i == 0:
				t = (self._ELEMENT, l[i])
				print t
				ll.append(t)
			if bp and i != 0:
				t = (self._PIN, l[i])
				print t
				ll.append(t)
			if bv:
				t = (self._VALUE, l[i])
				print t
				ll.append(t)
		if not ll:
			return None
		else:
			return ll



