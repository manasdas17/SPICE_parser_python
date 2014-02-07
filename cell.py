import utils
import collections

class Cell(object):
	_name = ""
	_pins = []
	_instance_count = 0
	_instancie_list = []
	_start = 0
	_end = 0
	_dict = collections.OrderedDict()
	def set_dictionary(self, a):
		self._dict = a.get_dictionary()
	def set_name(self, s):
		self._name = s
	def get_name(self):
		return self._name
	def set_pin_order(self, s):
		l = utils.format_input_string(s)
		self._pins = l
		del self._dict[self._start][2:]
		self._dict[self._start][2:] = l 
	def set_pin_order_with_list(self, l):
		del self._pins[2:]
		self._pins[2:] = l
		del self._dict[self._start][2:]
		self._dict[self._start][2:] = l 
	def get_pin_order(self):
		return self._pins
	def set_start(self, s):
		self._start = s 
	def get_start(self):
		return self._start
	def set_end(self, e):
		self._end = e 
	def get_end(self):
		return self._end
#	def get_all_instances(self, n):
		
