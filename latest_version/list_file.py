import os
import re
from tree import node
from tree import tree

def build_file_tree(rootDir):
	cPath = rootDir.getfpath()+rootDir.getdata()
	cList = os.listdir(cPath)
	cPath += "/"
	nodeList = []
	for item in cList:
		# pdb.set_trace()
		if isgit(item):
			continue
		if os.path.isfile(cPath+item):
			cfile = node(item)
			cfile.setfpath(cPath)
			rootDir.add(cfile)
		else:
			nextdir = node(item)
			nextdir.setfpath(cPath)
			build_file_tree(nextdir)
			rootDir.add(nextdir)
def isgit(cList):
	pattern = re.compile(r"\.git+")
	return pattern.match(cList)