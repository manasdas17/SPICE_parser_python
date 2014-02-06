
import net_list
import lex
from pprint import pprint

if __name__ == "__main__":
	netlist = net_list.NetList()
	lex = lex.Lexer()
	st = netlist.read("test.spx_2")
	s = lex._parse_one_line(st)
#	pprint(s)
#	print s[4][0]
#	print s

