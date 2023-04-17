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

def print_path (path):
    """Assume path is a list of nodes"""
    result =''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) -1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes;
    path are shortest are list of nodes. Return a shortest path from start to end in graph"""
    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))

    if start == end:
        return   path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest
def BFS (graph, start, end, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes. Returns a shortes path from start to end in graph"""
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        #Get and remove oldest elemenet in path_queue
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS Path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.childrenOf(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None

def shortest_path_DFS(graph, start, end, to_print = False):
    '''Assumes graph is a Digraph ; start and end are nodes. Return shortest path from start to end in graph'''
    return DFS(graph, start, end, [], None, to_print)

def shortest_path_BFS(graph, start, end, to_print = False):
    '''Assumes graph is a Digraph ; start and end are nodes. Return shortest path from start to end in graph'''
    return BFS(graph, start, end, to_print)
def test_SP():
    nodes=[]
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()

    for n in nodes:
        g.addNode(n)
    g.addEdge ( Edge ( nodes[ 0 ],nodes[ 1 ] ) )
    g.addEdge ( Edge ( nodes[ 1 ],nodes[ 2 ] ) )
    g.addEdge ( Edge ( nodes[ 2 ],nodes[ 3 ] ) )
    g.addEdge ( Edge ( nodes[ 2 ],nodes[ 4 ] ) )
    g.addEdge ( Edge ( nodes[ 3 ],nodes[ 4 ] ) )
    g.addEdge ( Edge ( nodes[ 3 ],nodes[ 5 ] ) )
    g.addEdge ( Edge ( nodes[ 0 ],nodes[ 2 ] ) )
    g.addEdge ( Edge ( nodes[ 1 ],nodes[ 0 ] ) )
    g.addEdge ( Edge ( nodes[ 3 ],nodes[ 1 ] ) )
    g.addEdge ( Edge ( nodes[ 3 ],nodes[ 4 ] ) )
    sp = shortest_path_BFS(g, nodes[0], nodes[5], to_print=True)
    print('shortest path found by DFS:', print_path(sp))

