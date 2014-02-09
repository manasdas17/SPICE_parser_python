
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
	o = netlist.get_cell("NR2_V20_3")
	o.set_dictionary(a)
	pins = o.get_pin_order()
	pp = 'VS GND VSS VDD MOFSET'
	o.set_pin_order(pp)
	r = o.get_pin_order()
	print "CELL PIN ORDER", r
	rr = o.get_pins()
	print rr
	t = o.get_instance("XMNA1")
	if t != None:
		print t.get_name()
		print t.get_pins()
		t.set_pin("D", "VDD")
		print t.get_pins()
		t.set_model("nch_2")
		print t.get_model()
		attr_name = t.get_attribute("spba1")
#	print "ATTR", attr_name
#	attrs = t.get_attributes()
#	print "AAAAAAA", attrs
#	t.set_attribute("w", 111)
#	attrs = t.get_attributes()
#	print "AAAAAAA", attrs
		print t.get_attribute("w")
		t.set_pin("S", "MOFSET")
		print "PINS", t.get_pins()
		t.set_attribute("w", 22)
		attrs = t.get_attributes()
		print "BBBBBB", attrs
		print "START", t.get_start()
	c = o.get_instance("C10")
	if c != None:
		print "C10 PINS", c.get_pins()
#	n = c.get_name()
#	print "CAPACITOR", c.get_name()
	print "FDFSFSDF", d
	inst_list = o.get_all_instances()
	print inst_list
	r = o.get_instance("R1")
	print d
	if r != None:
		print "R=", r.get_name(), r.get_start()
		r.set_name("RR1")
		print "PINS", r.get_pins()
		print "RES NAME", r.get_name()
	print d
#	print d[16]
#	print d[17][0][1]
#	print "dddd", d[18]
#	print r
#	print "asda", d[4][1][0]
#	print d[4][0][0][0]
#	print d[4][0][0][1]
#	print d[4][1][0]
#	print d[4][1][1]
#	print d[5][0][1]
	
#	print "aaa", d[1]

