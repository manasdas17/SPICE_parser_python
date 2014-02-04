
import codecs

class NetList(object):
	def read(self, file_name):
		f = open(file_name, "r+")
#		f = codecs.open(file_name, encoding='latin-1', mode='r+')
		st = f.read()
#		st.strip()
		return st


if __name__ == "__main__":
	netlist = NetList()
	st = netlist.read("test.spx")
#	st.decode('utf-8-sig')
#	print st


