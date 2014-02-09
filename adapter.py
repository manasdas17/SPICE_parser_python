
import lex
import collections

class Adapter(object):
	_dict = collections.OrderedDict()
	def __init__(self, fr):
		l = lex.Lexer()
		self._dict = l._parse_one_line(fr)
	def set_dictionary(self, d):
		self._dict = d
	def get_dictionary(self):
		return self._dict
