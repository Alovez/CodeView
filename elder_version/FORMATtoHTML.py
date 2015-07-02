import os

def  tohtml(aPathList,contentList,savePath,bookName):
	countfile = 0
	manifest = []
	spine = []
	CODE = open("template/code.Template")
	CODEtemp = CODE.readlines()
	CODE.close()
	CODEhead = CODEtemp[0:8]
	CODEback = CODEtemp[8:]	
	for cname in aPathList:
		
		if cname[-1:] == "/":
			filename = contentList[countfile]
			filename = filename[0:-1]+".html"
			manifest.append('<item id="chap'+str(countfile)+'" href="'+filename+'" media-type="text/html"/>\n')
			spine.append('<itemref idref="chap'+str(countfile)+'"/>\n')
			wfile = open(savePath+filename,"w")
			wfile.writelines(CODEhead)
			wfile.write("<h3>"+filename[0:-5]+"</h3>/n")
			wfile.writelines(CODEback)
			wfile.close()
			countfile+=1
			continue
		else:
			filename = contentList[countfile]+".html"
			manifest.append('<item id="chap'+str(countfile)+'" href="'+filename+'" media-type="text/html"/>\n')
			spine.append('<itemref idref="chap'+str(countfile)+'"/>\n')
			cfile = open(cname,"r")
			ws = cfile.readlines()
			wfile = open(savePath+filename,"w")
			wfile.writelines(CODEhead)
			wfile.writelines(ws)
			wfile.writelines(CODEback)
			cfile.close()
			wfile.close()
		countfile+=1

	OPF = open("template/opf.Template")
	OPFtemp = OPF.readlines()
	OPF.close()
	OPFhead1 = OPFtemp[0:6]
	OPFhead2 = OPFtemp[6:26]
	OPFmid = OPFtemp[27:29]
	OPFback = OPFtemp[30:]
	opf  = open(savePath+"content.opf","w")
	opf.writelines(OPFhead1)
	opf.write(bookName)
	opf.writelines(OPFhead2)
	opf.writelines(manifest)
	opf.writelines(OPFmid)
	opf.writelines(spine)
	opf.writelines(OPFback)