
import net_list
import lex
from pprint import pprint

if __name__ == "__main__":
	netlist = net_list.NetList()
	lex = lex.Lexer()
	st = netlist.read("test.spx_2")
	s = lex._parse_one_line(st)
	netlist.set_dictionary(s)
#	pprint(s)
#	print s[4][0]
#	print s[1][0]
#	ss = _get_cell_start_offset(s, "NR2_V20_2")
#	print s[9][1][1]
#	print ss
#	t = netlist._find_cell_by_name(s, "NR2_V20_2")
#	print t
#	ss = netlist._get_cell_end_offset(s, 1, "NR2_V20_1")
#	print s[9][1][1]
#	print s[19]
#	print ss
	ss = netlist._find_cell_by_name("NR2_V20_2")
	print ss



