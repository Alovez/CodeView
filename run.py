import os
from tree import node
from tree import tree
import list_file
import pdb

rootdir = node("")
rootdir.setfpath("C:/UserApp/wireshark")
list_file.build_file_tree(rootdir)
dirTree = tree()
dirTree.linktohead(rootdir)
l = dirTree.ergodic(rootdir)
for step in l:
	print step.getfpath() + step.getdata()

