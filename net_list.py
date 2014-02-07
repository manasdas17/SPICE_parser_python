
import codecs
import collections

class NetList(object):
	_dict = collections.OrderedDict()
	def read(self, file_name):
		f = open(file_name, "r+")
		st = f.read()
		if st.startswith(codecs.BOM_UTF8):
			st = st.lstrip(codecs.BOM_UTF8)
		return st
	def set_dictionary(self, d):
		self._dict = d
	def get_dictionary(self):
		return self._dict
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

#	def _generate_cell(self, d, i):
#	def generate_cells(self, d):


if __name__ == "__main__":
	netlist = NetList()
	st = netlist.read("test.spx")


