
import net_list
import lex

if __name__ == "__main__":
	netlist = net_list.NetList()
	lex = lex.Lexer()
	st = netlist.read("test.spx_2")
	s = lex._parse_one_line(st)
	print s[1]

