import os

def  tohtml(aPathList,contentList,savePath,bookName):
	countfile = 0
	opfhead = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE package PUBLIC "+//ISBN 978-7-308-05831-5//DTD OEB 1.2 Package//EN" "http://openebook.org/dtds/oeb-1.2/oebpkg12.dtd">
<package unique-identifier="bookid" xmlns:opf="http://www.idpf.org/2007/opf" xmlns="http://www.idpf.org/2007/opf" version="2.0">
	<metadata>
		<dc-metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		<dc:title>"""
	opfhead2 = """</dc:title>
		<dc:creator>安瑞</dc:creator>
		<dc:subject>杂文</dc:subject>
		<dc:description/>送大四的活动稿记述<dc:description/>
		<dc:publisher>AloveZ出版社</dc:publisher>
		<dc:date>2015-06</dc:date>
		<dc:type>杂文</dc:type>
		<dc:format>Text/html(.html,.htm)</dc:format>
		<dc:identifier id="bookid" opf:scheme="ISBN"></dc:identifier>
		<dc:language>en-US</dc:language>
		<dc:rights>AloveZ提供支持，原代码可发者持有版权</dc:rights>
		<dc:contributor/>
		<dc:source/>
		<dc:relation/>
		<dc:coverage/>
		<x-metadata/>
	</metadata>
	<manifest>
		<item id="cimage" media-type="image/jpeg" href="test.jpg" properties="cover-image"/>
		<item id="toc" properties="nav" href="content.html" media-type="text/html"/>"""
	head = """<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="content-type" content="text/html; charset=utf-8">\n<title>listfile.py</title>\n</head>\n<body>\n<pre>\n"""
	back = """</pre>\n</body>\n</html>\n"""
	opf  = open(savePath+"content.opf","w")
	opf.write(opfhead+bookName+opfhead2)

	for cname in aPathList:
		if cname[-1:] == "/":
			countfile+=1
			continue
		else:
			print contentList[countfile]
			print cname
			cfile = open(cname,"r")
			ws = cfile.readlines()
			wfile = open(savePath+contentList[countfile]+".html","w")
			wfile.write(head)
			wfile.writelines(ws)
			wfile.write(back)
			cfile.close()
			wfile.close()
		countfile+=1


