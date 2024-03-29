
import collections

class Resistor(object):
	_TYPE = "RESISTOR"
	_name = None
	_pins = []
	_attributes = [[]]
	_values = []
	_dict = collections.OrderedDict()
	_start = None
	def set_dictionary(self, a):
		self._dict = a.get_dictionary()
	def set_name(self, n):
		if n != None:
			self._name = n
			self._dict[self._start][0][1] = n
	def get_name(self):
		return self._name
	def set_values(self, v):
		self._values = v
	def get_values(self):
		return self._values
	def set_start(self, s):
		self._start = s
	def get_start(self):
		return self._start
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
