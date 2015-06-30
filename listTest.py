def listtest(tlist):
	tlist.append("1")
	listtest(tlist)



inlist = ["0"]
listtest(inlist)

print inlist