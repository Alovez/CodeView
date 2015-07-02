import os
from tree import node
from tree import tree

def writeContent(bookname, dirtree):
	headnode = dirtree.gethead()
	temp = open("template/content.Template")
	templines = temp.readlines()
	temp.close()
	lines = templines[0:7]
	lines.append("<h2>" + bookname + "</h2>\n")
	lines.append("<ol>\n")
	lines.extend(contentlines(headnode, dirtree))
	lines.append("</ol>\n")
	lines.extend(templines[7:])
	contentPath = headnode.getfpath()+"/content.html"
	content = open(contentPath,"w")
	content.writelines(lines)
	content.close()
	
def writeOPF(bookname, dirtree):
	headnode = dirtree.gethead()
	temp = open("template/opf.Template")
	templines = temp.readlines()
	temp.close()
	lines = templines[0:5]
	lines.append("<dc:title>"+bookname+"</dc:title>\n")
	lines.extend(templines[5:24])
	m, s = opflines(dirtree,headnode)
	lines.extend(m)
	lines.extend(templines[24:27])
	lines.extend(s)
	lines.extend(templines[27:])
	opfPath = headnode.getfpath()+"/"+bookname+".opf"
	opf = open(opfPath, "w")
	opf.writelines(lines)
	opf.close()

def tohtml(dirtree):
	headnode = dirtree.gethead()
	temp = open("template/code.Template")
	templines = temp.readlines()
	temp.close()
	codelines(dirtree, headnode, templines)

def contentlines(cnode, dirtree):
	wlist = []
	flist = cnode.getchildren()
	for step in flist:
		name = step.getdata()
		path = dirtree.relativepath(step)+".html"
		wlist.append("<li><a href='"+path+"'>"+name+"</a>\n")
		if step.getdegree() != 0:
			wlist.append("<ol>\n")
			wlist.extend(contentlines(step, dirtree))
			wlist.append("</ol>\n")
		wlist.append("</li>\n")
	return wlist

def opflines(dirtree, headnode):
	manifestlist = []
	snipe = []
	counter = 0
	l = dirtree.ergodic(headnode)
	for step in l:
		counter+=1
		href = dirtree.relativepath(step)+".html"
		n = str(counter)
		manifestlist.append('<item id="chap'+n+'" href="'+href+'" media-type="text/html"/>\n')
		snipe.append('<itemref idref="chap'+n+'"/>\n')	
	return manifestlist, snipe

def codelines(dirtree, headnode, templines):
	l = dirtree.ergodic(headnode)
	for step in l:
		codepath = step.getfpath()+step.getdata()
		if step.getdegree() != 0:
			wline = ["dir of \n",step.getdata()+"\n"]
		else:			
			code = open(codepath)
			wline = code.readlines()
			code.close()
		wcode = open(codepath+".html", "w")
		wcode.writelines(templines[0:8])
		wcode.writelines(wline)
		wcode.writelines(templines[8:])
		wcode.close()
