
import codecs
import collections
import cell
import adapter
#import resistor
#import capacitor
#import diode
import transistor

class NetList(object):
	_dict = collections.OrderedDict()
	def read(self, file_name):
		f = open(file_name, "r+")
		st = f.read()
		if st.startswith(codecs.BOM_UTF8):
			st = st.lstrip(codecs.BOM_UTF8)
		return st
	def set_dictionary(self, a):
		self._dict = a.get_dictionary()
		self._a = a
	def _get_cell_start_offset(self, n):
		for e in self._dict:
			if e != 0 and self._dict[e][0][1] == ".SUBCKT" and self._dict[e][1][1] == n:
				return e
	def _get_cell_end_offset(self, s, n):
		for e in sorted(self._dict.keys())[s:]:
			if e != 0 and self._dict[e][0][1] == ".ends" and self._dict[s][1][1] == n:
				return e
	def _find_cell_by_name(self, n):
		s = self._get_cell_start_offset(n)
		e = self._get_cell_end_offset(s, n)
		t = (s, e)
		return t
	def _generate_cell_object(self, t):
		o = cell.Cell()
		o.set_dictionary(self._a)
		o.set_start(t[0])
		o.set_end(t[1])
		name = self._dict[t[0]][1][1]
		o.set_name(name)
		l = self._dict[t[0]][2:]
		o.set_pin_order_with_list(l)
		return o
	def get_cell(self, n):
		t = self._find_cell_by_name(n)
		o = self._generate_cell_object(t)
		inst = self._generate_all_instances_in_cell(t)
		o.set_instance(inst)
#		print l[0].get_type()
		return o
	def _generate_all_instances_in_cell(self, t):
		instances = []
		s = t[0]
		pins = []
		attributes = []
		tr = transistor.Transistor()
		for i in sorted(self._dict.keys())[s:]:
			if self._dict[i][0][1] != ".ends":
				if self._dict[i][0][0][0] == "ELEMENT" and self._dict[i][0][0][1] == "TRANSISTOR":
					tr.set_name(self._dict[i][0][1])
					l = self._dict[i]
					tr.set_model(l[5][1])
					for i in xrange(len(l[1:])):
						if l[i][0] == "PIN" and i != 5:
							pins.append(l[i][1])
					tr.set_pins(pins)
					for i in xrange(len(l)):
						if l[i][0] == "ATTRIBUTE":
							attributes.append(l[i][1])
							tt = l[i][1]
							attr_name = l[i][1][0]
							attr_value = l[i][1][1]
					tr.set_attributes(attributes)
		instances.append(tr)
		return instances

					




