from enum import Enum
from optparse import Option
from typing import Any
from typing import Dict, List
from typing import Optional
from queue import Queue as test
from graphviz import Digraph as Groph


class Vertex:
    data: Any
    index: int

    def __init__(self, data, ind):
        self.data = data
        self.index = ind

    def __repr__(self):
        return f'{self.data}:v{self.index}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

    def __repr__(self):
        return f'{self.destination}'


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()

    def __repr__(self):
        stirng = ""
        for data in self.adjacencies:
            stirng += f'- {data} ->{self.adjacencies[data]}\n'
        return stirng

    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = list()

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        queue = test.Queue()
        queue.enqueue(list_keys[0])
        while (len(queue) != 0):
            new = queue.dequeue()
            list_visited.append(new)
            visit(new)
            for new_neighbour in self.adjacencies[new]:
                if new_neighbour.destination in list_visited:
                    True
                else:
                    queue.enqueue(new_neighbour.destination)

    def traverse_depth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        self._dfs(list_keys[0], list_visited, visit)

    def _dfs(self, v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for new_neighbour in self.adjacencies[v]:
            if new_neighbour.destination in visited:
                True
            else:
                self._dfs(new_neighbour.destination, visited, visit)

    def show(self, name="graph"):
        dot = Groph()
        visited=[]
        for x in self.adjacencies.keys():
            self._show_helper(x, dot, visited)
        dot.render(f'lab7/{name}',view=True, format="png",quiet_view=False)

    def _show_helper(self, v: Vertex, dot, visited: List):
        if v in visited:
            True
        else:
            dot.node(str(v.index), str(v.data))
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                desc=""
                if neighbour.weight != None:
                    desc+=f"{neighbour.weight}"
                dot.edge(str(neighbour.source.index), str(neighbour.destination.index), label=desc)
                if not(neighbour.destination in visited):
                    self._show_helper(neighbour.destination, dot, visited)


# DFS implementation to check if the path is dead
def dead_path(g: Graph, cross_id: Any) -> Optional[List[Vertex]]:
    vertices = g.adjacencies.keys()

    # Find vertex by cross_id
    cross_vertex = next(iter([v for v in vertices if v.data == cross_id]))

    # Find path where start and end is the same vertex
    path = dfs(g, cross_vertex, cross_vertex, [])
    if path is None:
        return None

    # Extract data from vertex
    path_data = [v.data for v in path]
    return path_data

def dfs(g: Graph, start: Vertex, end: Vertex, path: List[Vertex]) -> Optional[List[Vertex]]:
    path.append(start)

    # Check every vertex
    for edge in g.adjacencies[start]:
        dest = edge.destination

        # Check if we found the end vertex
        if dest == end:
            path.append(dest)
            return path

        # Check if we traverse the same vertex path if so, ignore
        if dest not in path:
            # Call recursive dfs
            result_path = dfs(g, dest, end, path)

            if result_path is not None:
                return result_path

    path.pop()
    return None
    


def lab():
    graph = Graph()
    names = [
        'Oczapowskiego',
        'Licznerskiego',
        'Prawochenskiego',
        'Heweliusza',
        'Warszawska',
        'Tuwima',
        'Kanafojskiego',
        'Absolwentow',
        'Sloneczna',
        'Zodiakalna',
        'Gwiezdna',
        'Iwaszkiewicza'
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Oczapowskiego'], vertices['Licznerskiego'])
    graph.add(EdgeType.directed, vertices['Oczapowskiego'], vertices['Prawochenskiego'])
    graph.add(EdgeType.directed, vertices['Oczapowskiego'], vertices['Heweliusza'])
    graph.add(EdgeType.directed, vertices['Warszawska'], vertices['Heweliusza'])
    graph.add(EdgeType.directed, vertices['Warszawska'], vertices['Tuwima'])
    graph.add(EdgeType.directed, vertices['Tuwima'], vertices['Sloneczna'])
    graph.add(EdgeType.directed, vertices['Zodiakalna'], vertices['Gwiezdna'])
    graph.add(EdgeType.directed, vertices['Iwaszkiewicza'], vertices['Sloneczna'])
    graph.add(EdgeType.directed, vertices['Kanafojskiego'], vertices['Oczapowskiego'])
    graph.add(EdgeType.directed, vertices['Sloneczna'], vertices['Absolwentow'])
    graph.add(EdgeType.directed, vertices['Zodiakalna'], vertices['Iwaszkiewicza'])
    graph.add(EdgeType.directed, vertices['Kanafojskiego'], vertices['Warszawska'])
    graph.add(EdgeType.directed, vertices['Gwiezdna'], vertices['Kanafojskiego'])
    graph.add(EdgeType.directed, vertices['Prawochenskiego'], vertices['Gwiezdna'])
    graph.add(EdgeType.directed, vertices['Sloneczna'], vertices['Kanafojskiego'])
    graph.add(EdgeType.directed, vertices['Gwiezdna'], vertices['Iwaszkiewicza'])

    path = dead_path(graph, 'Gwiezdna')
    print(path)

    path = dead_path(graph, 'Prawochenskiego')
    print(path)

    path = dead_path(graph, 'Heweliusza')
    print(path)

    path = dead_path(graph, 'Absolwentow')
    print(path)

    path = dead_path(graph, 'Sloneczna')
    print(path)

    graph.show(name="graph")


def test1():
    graph = Graph()
    names = [
        'Zabka',
        'Lidl',
        'Aldi',
        'Carrefour',
        'Auchan',
        'Intermarche',
        'Netto',
        'Biedronka',
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Zabka'], vertices['Biedronka'])
    graph.add(EdgeType.directed, vertices['Carrefour'], vertices['Auchan'])
    graph.add(EdgeType.directed, vertices['Auchan'], vertices['Netto'])
    graph.add(EdgeType.directed, vertices['Netto'], vertices['Carrefour'])
    graph.add(EdgeType.directed, vertices['Intermarche'], vertices['Zabka'])
    graph.add(EdgeType.directed, vertices['Aldi'], vertices['Biedronka'])
    graph.add(EdgeType.directed, vertices['Biedronka'], vertices['Biedronka'])
    graph.add(EdgeType.directed, vertices['Auchan'], vertices['Intermarche'])
    graph.add(EdgeType.directed, vertices['Aldi'], vertices['Lidl'])
    graph.add(EdgeType.directed, vertices['Zabka'], vertices['Aldi'])

    print(dead_path(graph, 'Biedronka'))
    print(dead_path(graph, 'Zabka'))
    print(dead_path(graph, 'Lidl'))
    print(dead_path(graph, 'Netto'))
    print(dead_path(graph, 'Auchan'))

    graph.show(name="test1")


def test2():
    graph = Graph()
    names = [
        'Ratuszowa',
        'Dworcowa',
        'Wyzwolenia',
        'Niepodleglosci',
        'Dluga',
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Ratuszowa'], vertices['Dworcowa'])
    graph.add(EdgeType.directed, vertices['Dworcowa'], vertices['Wyzwolenia'])
    graph.add(EdgeType.directed, vertices['Ratuszowa'], vertices['Wyzwolenia'])
    graph.add(EdgeType.directed, vertices['Wyzwolenia'], vertices['Dluga'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Ratuszowa'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Niepodleglosci'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Dworcowa'])

    print(dead_path(graph, 'Ratuszowa'))
    print(dead_path(graph, 'Dworcowa'))
    print(dead_path(graph, 'Wyzwolenia'))
    print(dead_path(graph, 'Niepodleglosci'))
    print(dead_path(graph, 'Dluga'))

    graph.show(name="test2")

def test3():
    graph = Graph()
    names = [
        'Zolnierska',
        'Dluga',
        'Obiegowa',
        'Pilsudskiego',
        'Plater',
        'Kopernika',
        'Mickiewicza',
        'Partyzantow',
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Kopernika'], vertices['Partyzantow'])
    graph.add(EdgeType.directed, vertices['Obiegowa'], vertices['Pilsudskiego'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Pilsudskiego'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Kopernika'])
    graph.add(EdgeType.directed, vertices['Dluga'], vertices['Zolnierska'])
    graph.add(EdgeType.directed, vertices['Partyzantow'], vertices['Zolnierska'])
    graph.add(EdgeType.directed, vertices['Mickiewicza'], vertices['Kopernika'])
    graph.add(EdgeType.directed, vertices['Kopernika'], vertices['Plater'])
    graph.add(EdgeType.directed, vertices['Obiegowa'], vertices['Partyzantow'])
    graph.add(EdgeType.directed, vertices['Zolnierska'], vertices['Mickiewicza'])

    print(dead_path(graph, 'Zolnierska'))
    print(dead_path(graph, 'Plater'))
    print(dead_path(graph, 'Obiegowa'))
    print(dead_path(graph, 'Mickiewicza'))
    print(dead_path(graph, 'Partyzantow'))
    print(dead_path(graph, 'Dluga'))

    graph.show(name="test3")

print("----- Lab7 -----")
lab()
print("\n----- test1 -----")
test1()
print("\n----- test2 -----")
test2()
print("\n----- test3 -----")
test3()