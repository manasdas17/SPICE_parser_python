
import net_list
import adapter
from pprint import pprint
import cell
import utils

if __name__ == "__main__":
	netlist = net_list.NetList()
#	lex = lex.Lexer()
	fr = netlist.read("test.spx_2")
	a = adapter.Adapter(fr)
#	s = lex._parse_one_line(fr)
	netlist.set_dictionary(a)
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
	d = a.get_dictionary()
#	print "DICTIONARY", d[8][0][1]
	o = netlist.get_cell("NR2_V20_2")
	o.set_dictionary(a)
	pins = o.get_pin_order()
	pp = 'GND VSS VDD'
	o.set_pin_order(pp)
	r = o.get_pin_order()
	print r
#	rr = o.get_pins()
#	print rr
	t = o.get_instance("XMNA1")
	print t.get_name()
	print t.get_pins()
	t.set_pin("D", "VDD")
	print t.get_pins()
	t.set_model("nch_2")
	print t.get_model()
#	print d[16]
#	print r
#	print "asda", d[4][1][0]
#	print d[4][0][0][0]
#	print d[4][0][0][1]
#	print d[4][1][0]
#	print d[4][1][1]
#	print d[5][0][1]
	
#	print "aaa", d[1]

