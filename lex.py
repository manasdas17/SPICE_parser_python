
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
	_PIN_PATTERN = '(^[a-zA-z]+[0-9]+[:][a-zA-Z0-9]+)'
	_ATTRIBUTE_PATTERN = '(^[a-zA-z_]+[0-9]+(\s)*[=](\s)*[a-z0-9.-]+)'
	_VALUE = '(^[0-9a-z.]+)'
	_NEW_LINE_PATTERN = '(^[+ ]+)'
	def _string_to_list(self, s):
		l = []
		l = s.split(" ")
		return l
	def _clear_line(self, s):
		tt = s.split()
		ss = ''.join(tt[0])
		if ss.startswith ("\xef\xbb\xbf") :
			t = ss.split("\xef\xbb\xbf")
			ss = ''.join(t)
			tt[0] = ss
			return ss
		return ss
	def _parse_one_line(self, s):
		buf = StringIO.StringIO(s)
		line = buf.readline()
	#	while line:
	#		line = buf.readline()
		return line
	#	return s
#	def _check_attribute(self, s):
	def _check_element(self, s):
		ss = self._clear_line(s)
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
				return "RESISTOR"
			if c:
				l = self._string_to_list(s)
		#		print l[0]
				self._make_tokens(l)
				return "CAPACITOR"
			if d:
				return "DIODE"
			if n:
				return "NEW LINE"
	def _make_tokens(self, l):
		for i in xrange(len(l)):
			print l[i]


