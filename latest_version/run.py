# -*- coding: utf8 -*-
import os
from tree import node
from tree import tree
import list_file
import format

gitpath = raw_input("git path:  ")
bookname = raw_input("bookname : ")
workpath = os.getcwd()
os.system("git clone " + gitpath + " ./"+bookname+"temp")

rootdir = node("")
rootdir.setfpath(workpath+"/"+bookname+"temp")
list_file.build_file_tree(rootdir)
dirTree = tree()
dirTree.linktohead(rootdir)

format.writeContent(bookname,dirTree)
format.writeOPF(bookname, dirTree)
format.tohtml(dirTree)

os.system("cp ./pi.jpg ./"+bookname+"temp/pi.jpg")
os.system("./kindlegen ./"+bookname+"temp/"+bookname+".opf")