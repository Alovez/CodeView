import os
import sys
import  re

def  listfile(startPath,spaceNum):
	currentList = []
	layerList = []
	currentFiles=os.listdir(startPath)
	pattern = re.compile(r"\.git+")
	i = 0
	while i < len(currentFiles):
		ford = currentFiles[i]
		#is file of git
		isgit = pattern.match(ford)
		if isgit:
			currentFiles.remove(ford)
			continue
		#is file or dir
		if os.path.isfile(startPath+"/"+ford):
			currentList.append(ford)
			layerList.append(spaceNum)
		else:
			currentList.append(ford)
			layerList.append(spaceNum)
			nextPath = startPath+"/"+ford
			nextList,nlayerList = listfile(nextPath,spaceNum+1)
			currentList.extend(nextList)
			layerList.extend(nlayerList)
		i+=1
	return currentList,layerList

def   writeContent(contentList,layerList,savePath,bookName):
	fileF = """<!DOCTYPE html>\n<html>\n<head>\n  <meta http-equiv="content-type" content="text/html; charset=utf-8">\n</head>\n<body>\n    <nav epub:type="toc">\n"""
	fileT = "<h2>"+bookName+"</h2>\n<ol>\n"
	contentFile = open(savePath+"/content.html","w")
	contentFile.write(fileF)
	contentFile.write(fileT)
	i = 0
	while i < len(contentList):
		cL = layerList[i]
		if i == len(contentList)-1:
			contentFile.write('<li><a href="' + cfile+ '.html">' + cfile + '</a></li>\n'+'</ol>\n'*(cL)+"</nav>\n</body>\n</html>")
			break
		nL = layerList[i+1]
		cfile = contentList[i]
		if cL == nL :
			contentFile.write('<li><a href="' + cfile+ '.html">' + cfile+ '</a></li>\n')
		elif cL < nL:
			contentFile.write('<li><a href="' + cfile+ '.html"><h3>' + cfile + '</h3></a></li>\n<ol>\n')
		elif cL > nL:
			contentFile.write('<li><a href="' + cfile+ '.html">' + cfile + '</a></li>\n'+'</ol>\n'*(cL - nL))
		i+=1
		
	# contentFile.write("</ol>\n"*(j-1)+"</nav>\n</body>\n</html>")