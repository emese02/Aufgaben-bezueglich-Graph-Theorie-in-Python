class DictGraph:
    """A not directed graph, represented as a map from each vertex to
    the set of neighbours"""

    def __init__(self, n):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges"""
        self._dict = {}
        for i in range(n):
            self._dict[i] = []

    def get_len_of_graph(self):
        return len(self._dict)

    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self._dict.keys()

    def neighbours(self, x):
        """Returns an iterable containing the neighbours of x"""
        return self._dict[x]

    def isEdge(self, x, y):
        """Returns True if there is an edge between x and y, False otherwise"""
        return y in self._dict[x]

    def addEdge(self, x, y):
        """Adds an edge between x to y.
        Precondition: there is no edge from x to y"""
        self._dict[x].append(y)
        self._dict[y].append(x)

    def printGraph(self):
        print(self._dict)

    def grad(self, x):
        return len(self._dict[x])

def von_datei_auslesen_nicht_gerichteten_Graph(datei_name):
    f = open(datei_name,"r")
    line = f.readline()
    knoten = int(line.strip())
    dict_graph = DictGraph(knoten)

    for line in f:
        edge = line.strip()
        x, y = edge.split(" ")
        x = int(x)
        y = int(y)
        dict_graph.addEdge(x,y)
    f.close()
    return dict_graph

def weg_finden(u, graph, besuchte_kante, weg=[]):
    weg = weg + [u]
    for v in graph.neighbours(u):
        if besuchte_kante[u][v] is False:
            besuchte_kante[u][v] = True
            besuchte_kante[v][u] = True
            weg = weg_finden(v, graph, besuchte_kante, weg)
    return weg

def pruefen_kreis(graph):
    # wir zaehlen die Knoten mit ungeraden Grad
    ungerade_knoten = 0
    i = -1
    for knoten in graph.parseX():
        if graph.grad(knoten) % 2 == 1:
            ungerade_knoten += 1
            i = knoten

    # falls alle Knoten sind mit ungeraden Grad -> eulersche Kreise nicht moeglich
    if ungerade_knoten == graph.get_len_of_graph() or ungerade_knoten == 1:
        return False, i
    return True, i

def kreis_finden(graph, start_knoten):
    len = graph.get_len_of_graph()
    # Am Anfang keine Knoten sind besucht
    besuchte_kante = [[False for i in range(len)] for j in range(len)]
    w = weg_finden(start_knoten, graph, besuchte_kante)
    print(w)

def main():
    g1 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei1.txt")
    enthaelt_kreis, i = pruefen_kreis(g1)
    if enthaelt_kreis is False:
        print("exisitiert eulersche Kreise nicht")
    else:
        if i!= -1:
            kreis_finden(g1,i)
        else:
            kreis_finden(g1,0)

main()