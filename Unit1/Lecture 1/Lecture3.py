# CLASS NODE
class Node ( object ):
    def __init__(self,name):
        ''' Assuming name is a string'''
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, scr, dest):
        """Assuming scr and dest are nodes"""
        self.scr = scr
        self.dest = dest
    def getSource(self):
        return self.scr
    def getDestionation(self):
        return self.dest
    def __str__(self):
        return self.scr.getName() + '> ' +self.dest.getName()

class Digraph(object):
    """edges is a dict mapping each node to a list of its children
    Nodes are represented as keys in dictionary
    Edges are represented by destinations as values in list associated with a source key"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError ('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestionation()

        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self,node):
        return self.edges[node]

    def hasNode(self,node):
        return node in self.edges

    def getNode(self,name):
        for n in self.edges:
            if n.getName ==name:
                return n
        raise NameError(name)
    def __str__(self):
        result =''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() +'\n'
        return result[:-1] # omit final newline

class Graph(Digraph):
    """Graph does not have directionality associated with an edge. Edge allow passage in either direction"""
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestionation(), edge.getSource())
        Digraph.addEdge(self,rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g