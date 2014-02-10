
import collections

class Transistor(object):
	_TYPE = "TRANSISTOR"
	_name = None
	_model = None
	_pins = []
	_attributes = [[]]
	_values = []
	_dict = collections.OrderedDict()
	_start = None
	def set_dictionary(self, a):
		self._dict = a.get_dictionary()
	def set_name(self, n):
		self._name = n
	def get_name(self):
		return self._name
	def set_model(self, m):
		self._model = m
		self._dict[self._start][5][1] = m
	def get_model(self):
		return self._model
	def set_start(self, s):
		self._start = s
	def get_start(self):
		return self._start
	def set_attribute(self, n, a):
		for i in sorted(self._dict.keys()):
			l = self._dict[i]
			if l != None:
				for j in xrange(len(l)):
					if(l[j][1][0] == n):
						self._dict[self._start][j][1][1] = a
						i = self._find_element_offset_in_attributes_list(n)
						self._attributes[i][1] = a
						return
	def _find_element_offset_in_attributes_list(self, n):
			for i in xrange(len(self._attributes)):
				if self._attributes[i][0] == n:
					return i
	def get_attribute(self, n):
		for i in xrange(len(self._attributes)):
			if self._attributes[i][0] == n:
				return self._attributes[i][1]
	def set_pins(self, p):
		self._pins = p
	def set_pin(self, n, v):
		if n == "S":
			self._pins[0] = v
			self._dict[self._start][1][1] = v
		if n == "D":
			self._pins[1] = v
			self._dict[self._start][2][1] = v
		if n == "G":
			self._pins[2] = v
			self._dict[self._start][3][1] = v
		if n == "B":
			self._pins[3] = v
			self._dict[self._start][4][1] = v
	def get_pin(self, n, v):
		if n == "S":
			return self._pins[0]
		if n == "D":
			return self._pins[1]
		if n == "G":
			return self._pins[2]
		if n == "B":
			return self._pins[3]
	def get_pins(self):
		return self._pins
	def set_attributes(self, l):
		self._attributes = l
	def get_attributes(self):
		return self._attributes
	def get_type(self):
		return self._TYPE
