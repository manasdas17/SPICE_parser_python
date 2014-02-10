
import codecs
import collections
import cell
import adapter
import resistor
import capacitor
#import diode
import transistor

class NetList(object):
	_dict = collections.OrderedDict()
	_output_file_name = None
	def read(self, file_name):
		f = open(file_name, "r+")
		st = f.read()
		if st.startswith(codecs.BOM_UTF8):
			st = st.lstrip(codecs.BOM_UTF8)
		f.close()
		return st
	def set_dictionary(self, a):
		self._dict = a.get_dictionary()
		self._a = a
	def _get_cell_start_offset(self, n):
		for e in self._dict:
			if e != 0 and self._dict[e] != None and self._dict[e][0][1] == ".SUBCKT" and self._dict[e][1][1] == n:
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
		return o
	def get_all_instances(self, start):
		inst_names = []
		t = (start,)
		inst = self._generate_all_instances_in_cell(t)
		for i in xrange(len(inst)):
			inst_names.append(inst[i].get_name())
		return inst_names
	def _get_all_cell_bounds(self):
		start = None
		end = None
		stack = []
		l = []
		t = ()
		for i in sorted(self._dict.keys()):
			l = self._dict[i]
			if not l:
				continue
			if self._dict[i][0][1] == ".SUBCKT":
				start = i
			if self._dict[i][0][1] == ".ends":
				end = i
			if start != None and end != None:
				t = (start, end)
				stack.append(t)
				start = None
				end = None
		return stack
	def _get_all_cells_objects(self):
		cell_list = []
		l = self._get_all_cell_bounds()
		for i in xrange(len(l)):
			t = l[i]
			o = self._generate_cell_object(t)
			cell_list.append(o)
		return cell_list
	def get_all_cells(self):
		out = []
		l = self._get_all_cells_objects()
		for i in xrange(len(l)):
			name = l[i].get_name()
			out.append(name)
		return out
	def _generate_all_instances_in_cell(self, t):
		instances = []
		s = t[0]
		pins = []
		values = []
		attributes = []
		for i in sorted(self._dict.keys())[s:]:
			if self._dict[i][0][1] == ".ends":
				break
			else: #self._dict[i][0][1] != ".ends":
				if self._dict[i][0][0][0] == "ELEMENT" and self._dict[i][0][0][1] == "TRANSISTOR":
					tr = transistor.Transistor()
					tr.set_dictionary(self._a)
					start = i
					tr.set_start(start)
					tr.set_name(self._dict[i][0][1])
					l = self._dict[i]
					tr.set_model(l[5][1])
					for j in xrange(len(l[1:])):
						if l[j][0] == "PIN" and j != 5:
							pins.append(l[j][1])
					tr.set_pins(pins)
					for k in xrange(len(l)):
						if l[k][0] == "ATTRIBUTE":
							attributes.append(l[k][1])
							tt = l[k][1]
							attr_name = l[k][1][0]
							attr_value = l[k][1][1]
					pins = []
					tr.set_attributes(attributes)
					instances.append(tr)
				if self._dict[i][0][0][0] == "ELEMENT" and self._dict[i][0][0][1] == "CAPACITOR":
					pins = []
					values = []
					cp = capacitor.Capacitor()
					cp.set_dictionary(self._a)
					start = i
					cp.set_start(start)
					cp.set_name(self._dict[i][0][1])
					l = self._dict[i]
					for h in xrange(len(l)):
						if l[h][0] == "PIN":
							pins.append(l[h][1])
						if l[h][0] == "VALUE":
							values.append(l[h][1])
					cp.set_values(values)
					cp.set_pins(pins)
					instances.append(cp)
				if self._dict[i][0][0][0] == "ELEMENT" and self._dict[i][0][0][1] == "RESISTOR":
					pins = []
					values = []
					rs = resistor.Resistor()
					rs.set_dictionary(self._a)
					start = i
					rs.set_start(start)
					rs.set_name(self._dict[i][0][1])
					l = self._dict[i]
					for h in xrange(len(l)):
						if l[h][0] == "PIN":
							pins.append(l[h][1])
						if l[h][0] == "VALUE":
							values.append(l[h][1])
					rs.set_values(values)
					rs.set_pins(pins)
					instances.append(rs)
		return instances
	def generate_netlist_output_file(self, n):
		l = []
		self._output_file_name = n
		f = open(self._output_file_name, "w+")
		for i in sorted(self._dict.keys()):
			if self._dict[i] != None:
				l = self._dict[i]
				temp = ''
				for j in xrange(len(l[0:])):
					if l[j][0] == "ATTRIBUTE":
						first = l[j][1][0]
						second = l[j][1][1]
						res = ''.join(l[j][1][0]) + ' = ' + ''.join(l[j][1][1])
						temp = temp + ' ' + res
					else:
						temp = temp + ' ' + ''.join(l[j][1])
				f.write(temp)
				f.write('\n')






					




