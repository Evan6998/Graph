import argparse

class Digraph(object):

    def __init__(self, v):
        if isinstance(v, int):
            self.loadWithInt = True
            self.v = v
            self.e = 0
            self.adj = [[] for i in range(v)]
            for i in range(self.v):
                self.adj[i] = []
        elif isinstance(v, file):
            self.loadWithInt = False
            self.v = int(v.readline())
            self.adj = [[] for i in range(self.v)]
            self.e = int(v.readline())
            for index, line in enumerate(v):
                self.addEdge(int(line.split()[0]), int(line.split()[1]))
    
    def getV(self):
        return self.v

    def getE(self):
        return self.e

    def getAdj(self):
        return self.adj

    def addEdge(self, v, w):
        self.adj[v].append(w)
        if self.loadWithInt:
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
    

