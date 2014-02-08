
class Resistor(object):
	_TYPE = "RESISTOR"
	_pins = []
	_attributes = []
	_values = []
	_name = None
	def set_name(self, n):
		_name = n
	def get_name(self):
		return _name
	def set_attribute(self, a):
		_attribute.append(a)
	def get_attributes(self):
		return _attribute
	def get_type(self):
		return _TYPE
