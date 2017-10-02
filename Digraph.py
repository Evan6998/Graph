class Digraph(object):

    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj = [None]*v
        for i in range(self.v):
            self.adj[i] = []
    
    def getV(self):
        return self.v

    def getE(self):
        return self.e

    def getAdj(self):
        return self.adj

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.e += 1

    def reserve(self):
        r = Digraph(self.v)
        for i in range(r.v):
            for w in self.adj:
                self.addEdge(w, r.v)
        return r

class DirectedDFS(object):
    def __init__(self, G, s):
        marked = [False] * G.v
    
    def Dire
