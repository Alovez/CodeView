from tree import node
import os

def aaaa(x):
	if x.getdata() == 2:
		return
	x.setdata(x.getdata()-1)
	x.add(node(7))
	aaaa(x)

cList = os.listdir("C:/UserApp/Fiddler2")
print cList
for s in cList:
	print os.path.isfile("C:/UserApp/Fiddler2/FiddlerHookBe.Windows.Forms.HexBox.dll")