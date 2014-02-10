
import net_list
import adapter
from pprint import pprint
import cell
import utils

if __name__ == "__main__":
	netlist = net_list.NetList()
	fr = netlist.read("test.spx")
	a = adapter.Adapter(fr)
	netlist.set_dictionary(a)
	d = a.get_dictionary()
	o = netlist.get_cell("OR4B_CV20G02_8")
	o.set_dictionary(a)
	print "get_pin_order: ", o.get_pin_order()
	o.set_pin_order('GND VSS VCC')
	print "get_pin_order: ", o.get_pin_order()
	start = o.get_start()
	print netlist.get_all_instances(start)
	print netlist.get_all_cells()
	t = o.get_instance("XMNA")
	if t != None:
		t.set_pin("S", "VDD")
		t.set_pin("B", "VBB")
		t.set_attribute("w", "0.14u")
		t.set_attribute("spba1", "111")
		t.set_model("MOSFET")
		print "get model: ", t.get_model()
	netlist.generate_netlist_output_file("output.spx")

