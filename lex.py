
import re
import StringIO
#from collections import defaultdict
from collections import OrderedDict
import collections
import utils

class Lexer(object):
	_ELEMENT = "ELEMENT"
	_PIN = "PIN"
	_ATTRIBUTE = "ATTRIBUTE"
	_VALUE = "VALUE"
	_START = "START"
	_END = "END"
	_TRANSISTOR = "TRANSISTOR"
	_RESISTOR = "RESISTOR"
	_CAPACITOR = "CAPACITOR"
	_DIODE = "DIODE"
	_CELL_START_PATTERN = '(.SUBCKT.*)'
	_CELL_END_PATTERN = '(^.ends)'
	_TRANSISTOR_PATTERN = '(^[X|m|M][0-9a-zA-Z_]+)'
	_RESISTOR_PATTERN = '(^[r|R][0-9a-zA-Z_]+)'
	_CAPACITOR_PATTERN = '(^[c|C][0-9a-zA-Z_]+)'
	_DIODE_PATTERN = '(^[d|D][0-9a-zA-Z_]+)'
	_ELEMENT_PATTERN = '(^[a-zA-z]+[a-zA-Z0-9]*)'
	_ATTRIBUTE_PATTERN = r'[\w_]+\s*=\s*[\w\.\-]+' 
#	_PIN_PATTERN = r'\w+\s*:?\s*\w*'
#	_PIN_PATTERN = r'(^[a-zA-Z]\w+\s*:?\s*\w*)'
	_PIN_PATTERN = r'(^[a-zA-Z].*\w*\s*:?\s*\w*)'
	_VALUE_PATTERN = '(^[0-9]+.?[0-9eu+-]+)'
	_VALUE_PATTERN_2 = '(=\w*.?\w*-?\w*)'
	_NEW_LINE_PATTERN = '(^[+ ]+)'
	_NAME_PATTERN = r'\w*\s*_?\s*\w*'
	def _parse_one_line(self, s):
		d = collections.OrderedDict()
		i = 0
		ll = []
		line_2 = ""
		buf = StringIO.StringIO(s)
		while True:
			line = buf.readline()
			if line:
				if line.startswith('*') or line == '' or line == '\n':
					continue
				if line.startswith('+'):
					line = utils.clean_string(line)
					line_2 = utils.clean_string(line_2)
					line = utils.merge_two_string(line_2, line)
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
	def _is_cell_start(self, s):
		a = re.match(self._CELL_START_PATTERN, s)
		if a:
			return True
		else:
			return False
	def _is_cell_end(self, s):
		a = re.match(self._CELL_END_PATTERN, s)
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
			return "Unrecognizable element"
		else:
			if t:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l, self._TRANSISTOR)
				return ll
			if r:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l, self._RESISTOR)
				return ll
			if c:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l, self._CAPACITOR)
				return ll
			if d:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l, self._DIODE)
				return ll
			if n:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			if cc:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l)
				return ll
			if ce:
				l = utils.string_to_list(s)
				ll = self._make_tokens(l)
				return ll
	def _make_tokens(self, l, etype = None):
		ll = []
		for i in xrange(len(l)):
			ba = self._is_attribute(l[i])
			be = self._is_element(l[i])
			bp = self._is_pin(l[i])
			bv = self._is_value(l[i])
			bn = self._is_new_line(l[i])
			bcs = self._is_cell_start(l[i])
			bce = self._is_cell_end(l[i])
			if ba:
				self._tokenize_attribute(l[i])
				tt = self._tokenize_attribute(l[i])
				lll = [self._ATTRIBUTE, tt]
				ll.append(lll)
				continue
			if be and i == 0:
				lll = [[self._ELEMENT, etype], l[i]]
				ll.append(lll)
				continue
			if bp and i != 0:
				lll = [self._PIN, l[i]]
				ll.append(lll)
				continue
			if bv:
				lll = [self._VALUE, l[i]]
				ll.append(lll)
				continue
			if bcs:
				lll = [self._START, l[i]]
				ll.append(lll)
				continue
			if bce:
				lll = [self._END, l[i]]
				ll.append(lll)
				continue
		if not ll:
			return None
		else:
			return ll



