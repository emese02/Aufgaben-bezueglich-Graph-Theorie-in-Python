class MatrGraph:
    """An undirected graph, represented by adjacency matrix.
    Vertices are numbers from 0 to n-1"""

    def __init__(self, n):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges"""
        self._n = n
        self._matr = []
        for i in range(n):
            self._matr.append([])
            for j in range(n):
                self._matr[i].append(False)

    def get_len_of_matrix(self):
        return len(self._matr)

    def parseX(self):
        """Returns an iterable containing all the vertices"""
        nrOfVertices = len(self._matr)
        return range(nrOfVertices)

    def parseN(self, x):
        """Returns an iterable containing the  neighbours of x"""
        list = []
        for i in range(len(self._matr[x])):
            if self._matr[x][i]:
                list.append(i)
        return list

    def isEdge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        return self._matr[x][y]

    def addEdge(self, x, y):
        """Adds an edge between x to y
        Precondition: there is no edge from x to y"""
        self._matr[x][y] = True
        self._matr[y][x] = True

    def printGraph(self):
        for i in range(self._n):
            print(self._matr[i][:])

    def grad(self, knoten):
        # Knoten sind von 0 bis n-1
        if knoten >= self._n:
            raise ValueError("Graph hat diesen Knoten nicht")
        else:
            return len (self.parseN(knoten))

def von_datei_auslesen_nicht_gerichteten_Graph(datei_name):
    f = open(datei_name,"r")
    line = f.readline()
    knoten = int(line.strip())
    adjazenz_graph = MatrGraph(knoten)

    for line in f:
        edge = line.strip()
        x, y = edge.split(" ")
        x = int(x)
        y = int(y)
        adjazenz_graph.addEdge(x, y)
    f.close()
    return adjazenz_graph

def durchschnitt(graph1, graph2):
    gemeinsame_knoten = min(graph1.get_len_of_matrix(), graph2.get_len_of_matrix())
    # graph3 wird der Durchschnitt sein
    graph3 = MatrGraph(gemeinsame_knoten)

    # wir uberprufen ob die Kanten in den kleinsten Graph kommen in die anderen Graph auch vor
    if graph1.get_len_of_matrix() == gemeinsame_knoten:
        for x in graph1.parseX():
            neighbours = graph1.parseN(x)
            for element in neighbours:
                if graph2.isEdge(x, element):
                    graph3.addEdge(x, element)
    else:
        for x in graph2.parseX():
            neighbours = graph2.parseN(x)
            for element in neighbours:
                if graph1.isEdge(x, element):
                    graph3.addEdge(x, element)

    return graph3

def main():
    g1 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei1.txt")
    g1.printGraph() ; print()
    g2 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei2.txt")
    g2.printGraph() ; print()
    g3 = durchschnitt(g1,g2)
    g3.printGraph()
main()