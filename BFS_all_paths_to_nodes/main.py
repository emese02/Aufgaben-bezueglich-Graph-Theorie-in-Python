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

def breitensuche_wege(graph, start_knoten):
    entdeckt = [start_knoten]
    besucht = []
    alle_wege =[[start_knoten]]

    prev =[]
    # fuer knoten
    while len(entdeckt)!=0:
        elem = entdeckt.pop(0)
        for knoten in graph.neighbours(elem):
            weg = [start_knoten]
            if knoten not in besucht and knoten not in entdeckt:
                entdeckt.append(knoten)
            weg.append(knoten)
           # prev [knoten] = weg
            alle_wege.append(weg)
        besucht.append(elem)


    alle_wege_reihenfolge = []
    for knoten in graph.parseX():
        gefunden = False
        for wege in alle_wege:
            if knoten in wege:
                alle_wege_reihenfolge.append(wege)
                gefunden = True
                break

        if not gefunden:
                alle_wege_reihenfolge.append("existiert nicht")

    return alle_wege_reihenfolge


def main():
    g1 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei1.txt")
    print(breitensuche_wege(g1, 1))

main()