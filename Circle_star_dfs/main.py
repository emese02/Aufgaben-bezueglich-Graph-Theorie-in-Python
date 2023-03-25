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

def uberpruft_ob_stern(graph):
    # wir zaehlen wie viele Knoten mit Grad 1 haben wir
    anzahl_der_knoten_mit_grad1 = 0
    for knoten in graph.parseX():
        if graph.grad(knoten) == 1:
            anzahl_der_knoten_mit_grad1 += 1
        else:
            knoten_mit_grad_verschieden_von1 = knoten

    # falls wir haben genau len_grap-1 Knoten mit Grad 1 und ein Knoten mit Grad len_graph - 1 => wir haben ein Stern
    len_grahp =  graph.get_len_of_graph()

    if anzahl_der_knoten_mit_grad1 == len_grahp - 1:
        if graph.grad(knoten_mit_grad_verschieden_von1) == len_grahp - 1:
            return True

    return False


def uberpruft_ob_kreis(graph):
    if graph.get_len_of_graph() <= 2:
        return False

    # fuer Kreis alle Knoten muessen Grad 2 haben, falls es gibt eine Ausnahme -> nicht Kreis

    for knoten in graph.parseX():
        if graph.grad(knoten)!= 2:
            return False

    # Tiefensuche, alle Knoten muessen besucht werden (1 Komponent)
    markierte = [0]
    for knoten in graph.parseX():
        for x in graph.neighbours(knoten):
            if x not in markierte and x != 0:
                markierte.append(x)

    if len(markierte) != graph.get_len_of_graph():
        return False

    return True

def main():
    g1 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei1.txt")
    g2 = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei2.txt")
    print("Graph1 Kreis: ", uberpruft_ob_kreis(g1))
    print("Graph2 Kreis: ", uberpruft_ob_kreis(g2))
    print("Graph1 Stern: ", uberpruft_ob_stern(g1))
    print("Graph2 Stern: ", uberpruft_ob_stern(g2))
main()