
import StringIO
import re

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
	_PIN_PATTERN = '(^[a-zA-z]+[0-9]*[:]?[a-zA-Z0-9]*)'
	_ATTRIBUTE_PATTERN = '(^[a-zA-z_]+[0-9]+(\s)*[=](\s)*[a-z0-9.-]+)'
	_VALUE_PATTERN = '(^[0-9a-z.+-]+)'
	_NEW_LINE_PATTERN = '(^[+ ]+)'
	def _string_to_list(self, s):
		l = []
		l = s.split(" ")
		return l
	def _clear_line(self, s):
		if s.startswith ("\xef\xbb\xbf") :
			print s
			s = s.rstrip("\xef\xbb\xbf")
			l = s.split()
			print l
		if s.endswith("\r\n") :
			print s
			s = s.rstrip("\r\n")
			l = s.split()
			print l
		return s
#	def _clear_line(self, s):
#		tt = s.split()
#		ss = ''.join(tt[0])
#		if ss.startswith ("\xef\xbb\xbf") :
#			t = ss.split("\xef\xbb\xbf")
#			ss = ''.join(t)
#			tt[0] = ss
#			return ss
#		return ss
	def _parse_one_line(self, s):
		buf = StringIO.StringIO(s)
		line = buf.readline()
	#	while line:
	#		line = buf.readline()
		return line
	#	return s
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
		if a:
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
#		ss = self._clear_line(s)
		ss = s
		t = re.match(self._TRANSISTOR_PATTERN, ss)
		r = re.match(self._RESISTOR_PATTERN, ss)
		c = re.match(self._CAPACITOR_PATTERN, ss)
		d = re.match(self._DIODE_PATTERN, ss)
		n = re.match(self._NEW_LINE_PATTERN, ss)
		if t == 0 and r == 0 and c == 0 and d == 0 and n == 0:
			return "Unrecognizable instructions"
		else:
			if t:
				print s
				return "TRANSISTOR"
			if r:
				l = self._string_to_list(s)
				self._make_tokens(l)
				print l[0].split()
				return "RESISTOR"
			if c:
				l = self._string_to_list(s)
				self._make_tokens(l)
				return "CAPACITOR"
			if d:
				return "DIODE"
			if n:
				return "NEW LINE"
	def _make_tokens(self, l):
		ll = []
		k = 0
		for i in xrange(len(l)):
			ba = self._is_attribute(l[i])
			be = self._is_element(l[i])
			bp = self._is_pin(l[i])
			bv = self._is_value(l[i])
#			if not ba and not bp and not bv:
#				return "Unrecognizable instructions"
#			else:
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
			return ll
		else:
			return None



