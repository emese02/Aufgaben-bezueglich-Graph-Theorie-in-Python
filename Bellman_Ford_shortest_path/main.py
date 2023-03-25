class DictGraph:
    """A directed graph, represented as a map from each vertex to
    the set of outbound neighbours"""

    def __init__(self, n):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges"""
        self._dict = {}
        for i in range(n):
            self._dict[i] = []
        self.costs =[]
        for i in range(n):
            self.costs.append([])
            for j in range(n):
                self.costs[i].append(0)

    def get_cost(self, x, y):
        """Cost between x and y"""
        return self.costs[x][y]

    def addCost(self, x, y, cost):
        self.costs[x][y] = cost

    def print_cost_matrix(self):
        for i in range(self.get_len_of_graph()):
            print(self.costs[i][:])

    def get_len_of_graph(self):
        return len(self._dict)

    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self._dict.keys()

    def parseNout(self, x):
        """Returns an iterable containing the outbound neighbours of x"""

    def parseNin(self, x):
        """Returns an iterable containing the inbound neighbours of x"""
        list = []
        for i in self._dict.keys():
            if x in self._dict[i]:
                list.append(i)
        return list

    def isEdge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        return y in self._dict[x]

    def addEdge(self, x, y):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""
        self._dict[x].append(y)

    def printGraph(self):
        print(self._dict)


def von_datei_auslesen_gerichteten_Graph(datei_name):
    f = open(datei_name,"r")
    line = f.readline()
    knoten = int(line.strip())
    dict_graph = DictGraph(knoten)

    for line in f:
        edge = line.strip()
        x, y, cost = edge.split(" ")
        x = int(x)
        y = int(y)
        cost = int(cost)
        dict_graph.addEdge(x,y)
        dict_graph.addCost(x,y,cost)
    f.close()
    return  dict_graph

def get_shortest_with_Bellman_Ford(graph, s, K):
    # s StartKnoten
    dist = []
    predecessor = []

    for knoten in graph.parseX():
        dist.insert(knoten, float('inf'))
        predecessor.insert(knoten, -1)

    dist[s] = 0
    n = graph.get_len_of_graph()

    for i in range (n-1):
        for u in graph.parseX():
            for v in graph.parseX():
                if graph.isEdge(u,v):
                    w = graph.get_cost(u,v)
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        predecessor[v] = u

    for u in graph.parseX():
        for v in graph.parseX():
            if graph.isEdge(u, v):
                w = graph.get_cost(u, v)
                if dist[u] + w < dist[v]:
                    raise ValueError("Graph contains a negative-weight cycle")

    weg = []
    x = K

    while x!=s:
        weg.append(predecessor[x])
        x = predecessor[x]

    # Liste invertieren
    weg = weg[::-1]
    weg.append(K)

    return dist,predecessor, dist[K], weg

def main():
    g1= von_datei_auslesen_gerichteten_Graph("graph_datei.txt")
    g1.printGraph()
    g1.print_cost_matrix()
    d,p,distance, predecessors = get_shortest_with_Bellman_Ford(g1,2,6)
    #print(d," ",p)
    print(" distance: ",distance,",  predecessors:", predecessors)
main()