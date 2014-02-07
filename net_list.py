
import codecs
import collections
import cell
import adapter

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
#		s = ''.join(l)
#		print l
		o.set_pin_order_with_list(l)
		return o
	def get_cell(self, n):
		t = self._find_cell_by_name(n)
		o = self._generate_cell_object(t)
		return o
