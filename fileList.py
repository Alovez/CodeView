import os
import sys
import  re
import getCONTENT



docPath =  "/home/a/Programing/git"
# docPath = input("input the start Path:  ")
docList,layerList = getCONTENT.listfile(docPath,1)
getCONTENT.writeContent(docList,layerList,"/home/a/Programing/","aaa")
for out in docList:
	print out
for out in layerList:
	print out
	# print out[0:1]




#error way to choose dir 
# isfile = pattern.match(ford)
# if not isfile:
# 	isgit = pattern2.match(ford)
# 	if  isgit:
# 		listfile.remove(ford)
# 		print ford,"is a git dir"
# 		continue
# 	else:
# 		print ford,"is a dir"
# 		listfile[i] = '-'+ford
# else:
# 	print ford,"is a file"


# def  listfile(startPath,spaceNum,cPath):
# 	currentList = []
# 	currentFiles=os.listdir(startPath)
# 	pattern = re.compile(r"\.git+")
# 	i = 0
# 	while i < len(currentFiles):
# 		ford = currentFiles[i]
# 		#is file of git
# 		isgit = pattern.match(ford)
# 		if isgit:
# 			currentFiles.remove(ford)
# 			continue
# 		#is file or dir
# 		if os.path.isfile(startPath+"/"+ford):
# 			currentList.append(str(spaceNum)+ford)
# 		else:
# 			currentList.append(str(spaceNum)+ford)
# 			nextPath = startPath+"/"+ford
# 			currentList.extend(listfile(nextPath,spaceNum+1,ford))
# 		i+=1
# 	return currentList