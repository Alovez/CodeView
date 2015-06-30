import os
import sys
import  re

def  listfile(startPath,spaceNum):
	currentList = []
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
			currentList.append("|   "*spaceNum+ford)
		else:
			currentList.append("|   "*spaceNum+"-"+ford)
			spaceNum+=1
			nextPath = startPath+"/"+ford
			currentList.extend(listfile(nextPath,spaceNum))
			spaceNum-=1
		i+=1
	return currentList


docPath =  "/home/a/Programing/Cutie"

docList = listfile(docPath,1)
for out in docList:
	print out




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