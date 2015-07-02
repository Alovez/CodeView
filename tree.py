class node:
 
    def __init__(self, data):   
        self._data = data
        self._children = []
        self._fpath = ""

    def setfpath(self,fp):
        self._fpath = fp

    def setdata(self, data):
        self._data = data
        
    def getdata(self):
        return self._data
 
    def getchildren(self):
        return self._children
 
    def getdegree(self):
        return len(self._children)

    def getfpath(self):
        return self._fpath

    def add(self, node):
        self._children.append(node)
 
    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None
 
class tree:
 
    def __init__(self):
        self._head = node('header')
 
    def linktohead(self, node):
        self._head.add(node)
 
    def insert(self, path, data):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return False
            else:
                cur = cur.go(step)
        cur.add(node(data))
        return True
 
    def search(self, path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return None
            else:
                cur = cur.go(step)
        return cur

    def ergodic(self, start):
        cur = start
        l = []
        for step in cur.getchildren():
            l.append(step)
            if step.getdegree != 0:
                nl = self.ergodic(step)
                l.extend(nl)
        return l
