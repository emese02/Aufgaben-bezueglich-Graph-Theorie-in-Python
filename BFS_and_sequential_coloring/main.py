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

def breitensuche(graph, start_knoten):
    entdeckt = [start_knoten]
    besucht = []
    while len(entdeckt)!=0:
        elem = entdeckt.pop(0)
        for knoten in graph.neighbours(elem):
            if knoten not in besucht and knoten not in entdeckt:
                entdeckt.append(knoten)
        besucht.append(elem)
    return  besucht

def sequentielle_faerbung(g):
    n = g.get_len_of_graph()

    # wir werden die Faerbung fur die Knoten in die List ergebnis speichern
    ergebnis = [-1 for i in range(n)]

    # wir merken wenn ist eine Farbe verfuegbar fuer Farben
    verfuegbare_faerbe = [True for i in range(n)]

    # wir setzen die Farbe erster Knoten
    l = breitensuche(g, 0)
    ergebnis[l[0]] = 0

    # wir bestimmen die Faerbungen fuer andere Knoten
    for knoten in l:
        if ergebnis[knoten] == -1:
            # falls ein Nachbarn ist schon gefaerbt -> nicht mehr verfuegbar fuer dem aktuellen Knoten
            for nachbarn in g.neighbours(knoten):
                if ergebnis[nachbarn] != -1:
                    verfuegbare_faerbe [ergebnis[nachbarn]] = False

            # wir suchen die erste verfuegbare Farbe
            index = 0
            while verfuegbare_faerbe[index] is False:
                index += 1

            # wir speichern die Faerbung
            ergebnis[knoten] = index

            # Verfuegbarkeit wiedersetzen
            for nachbarn in g.neighbours(knoten):
                if ergebnis[nachbarn] != -1:
                    verfuegbare_faerbe[ergebnis[nachbarn]] = True

    # gibt zurueck die Knoten-Farbe Paaren
    faerbung = [(knoten, ergebnis[knoten]) for knoten in range(n)]
    return faerbung

def main():
    graph = von_datei_auslesen_nicht_gerichteten_Graph("graph_datei2.txt")
    faerbung = sequentielle_faerbung(graph)
    for knoten, farbe in faerbung:
        print("Knoten ", knoten, "   ~    Farbe ", farbe)

main()