
class Transistor(object):
	_TYPE = "TRANSISTOR"
	_name = None
	_model = None
	_pins = []
	_attributes = [[]]
	_values = []
	def set_name(self, n):
		self._name = n
	def get_name(self):
		return self._name
	def set_model(self, m):
		self._model = m
	def get_model(self):
		return self._model
	def set_attribute(self, n, a):
		for i in xrange(len(self._attributes)):
			if self._attributes[i][0] == n:
				self._attributes[i][1] = a
	def get_attribute(self, n):
		for i in xrange(len(self._attributes)):
			if self._attributes[i][0] == n:
				return self._attributes[i][1]
	def set_pins(self, p):
		self._pins = p
	def set_pin(self, n, v):
		if n == "S":
			self._pins[0] = v
		if n == "D":
			self._pins[1] = v
		if n == "G":
			self._pins[2] = v
		if n == "B":
			self._pins[3] = v
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
