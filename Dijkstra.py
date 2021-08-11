class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def addEdge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        cur_wt = visited[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node

    return visited, path


def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route


if __name__ == '__main__':
    g = Graph()
    g.nodes = set(range(1, 100))
    g.addEdge(1, 2, 15)
    g.addEdge(1, 4, 10)
    g.addEdge(1, 13, 16)
    g.addEdge(1, 3, 21)
    g.addEdge(1, 42, 18)
    g.addEdge(2, 74, 28)
    g.addEdge(2, 6, 8)
    g.addEdge(2, 49, 17)
    g.addEdge(2, 5, 17)
    g.addEdge(2, 4, 16)
    g.addEdge(3, 42, 13)
    g.addEdge(3, 9, 12)
    g.addEdge(6, 7, 22)
    g.addEdge(6, 8, 23)
    g.addEdge(7, 49, 17)
    g.addEdge(7, 14, 22)
    g.addEdge(7, 8, 18)
    g.addEdge(7, 15, 23)
    g.addEdge(8, 16, 27)
    g.addEdge(8, 9, 31)
    g.addEdge(9, 45, 12)
    g.addEdge(9, 19, 51)
    g.addEdge(9, 23, 49)
    g.addEdge(9, 10, 21)
    g.addEdge(10, 46, 10)
    g.addEdge(10, 32, 12)
    g.addEdge(11, 39, 16)
    g.addEdge(11, 12, 15)
    g.addEdge(11, 44, 19)
    g.addEdge(12, 44, 17)
    g.addEdge(12, 26, 26)
    g.addEdge(13, 11, 14)
    g.addEdge(14, 86, 18)
    g.addEdge(14, 28, 25)
    g.addEdge(15, 85, 9)
    g.addEdge(15, 71, 15)
    g.addEdge(16, 17, 12)
    g.addEdge(16, 28, 22)
    g.addEdge(16, 33, 8)
    g.addEdge(17, 18, 19)
    g.addEdge(17, 45, 22)
    g.addEdge(18, 19, 24)
    g.addEdge(18, 23, 21)
    g.addEdge(18, 45, 21)
    g.addEdge(19, 61, 55)
    g.addEdge(20, 21, 5)
    g.addEdge(21, 22, 10)
    g.addEdge(21, 23, 8)
    g.addEdge(22, 25, 16)
    g.addEdge(22, 48, 18)
    g.addEdge(24, 27, 22)
    g.addEdge(25, 33, 17)
    g.addEdge(25, 38, 23)
    g.addEdge(25, 37, 22)
    g.addEdge(26, 43, 17)
    g.addEdge(26, 29, 20)
    g.addEdge(26, 47, 12)
    g.addEdge(26, 31, 12)
    g.addEdge(27, 34, 18)
    g.addEdge(27, 99, 39)
    g.addEdge(27, 61, 35)
    g.addEdge(28, 38, 22)
    g.addEdge(28, 59, 21)
    g.addEdge(29, 51, 7)
    g.addEdge(29, 41, 21)
    g.addEdge(30, 40, 15)
    g.addEdge(30, 34, 27)
    g.addEdge(32, 46, 12)
    g.addEdge(34, 50, 27)
    g.addEdge(35, 48, 16)
    g.addEdge(35, 56, 29)
    g.addEdge(36, 89, 25)
    g.addEdge(36, 39, 9)
    g.addEdge(36, 41, 11)
    g.addEdge(37, 38, 17)
    g.addEdge(37, 55, 18)
    g.addEdge(37, 48, 22)
    g.addEdge(38, 58, 23)
    g.addEdge(40, 43, 8)
    g.addEdge(40, 50, 15)
    g.addEdge(40, 30, 17)
    g.addEdge(41, 100, 12)
    g.addEdge(41, 53, 26)
    g.addEdge(43, 47, 6)
    g.addEdge(43, 31, 6)
    g.addEdge(43, 31, 6)
    g.addEdge(48, 60, 31)
    g.addEdge(51, 52, 13)
    g.addEdge(52, 66, 12)
    g.addEdge(52, 63, 45)
    g.addEdge(52, 78, 58)
    g.addEdge(53, 62, 22)
    g.addEdge(53, 89, 13)
    g.addEdge(54, 73, 27)
    g.addEdge(54, 57, 9)
    g.addEdge(54, 62, 20)
    g.addEdge(54, 74, 24)
    g.addEdge(55, 58, 11)
    g.addEdge(55, 70, 15)
    g.addEdge(56, 64, 29)
    g.addEdge(56, 65, 13)
    g.addEdge(57, 74, 18)
    g.addEdge(59, 83, 13)
    g.addEdge(60, 61, 42)
    g.addEdge(61, 99, 68)
    g.addEdge(62, 89, 26)
    g.addEdge(63, 82, 24)
    g.addEdge(65, 70, 33)
    g.addEdge(66, 95, 8)
    g.addEdge(66, 94, 30)
    g.addEdge(67, 68, 23)
    g.addEdge(67, 100, 17)
    g.addEdge(67, 75, 24)
    g.addEdge(68, 100, 23)
    g.addEdge(68, 69, 45)
    g.addEdge(69, 75, 12)
    g.addEdge(69, 79, 22)
    g.addEdge(69, 72, 32)
    g.addEdge(71, 74, 32)
    g.addEdge(72, 90, 17)
    g.addEdge(73, 90, 25)
    g.addEdge(75, 93, 14)
    g.addEdge(75, 94, 19)
    g.addEdge(76, 94, 12)
    g.addEdge(76, 92, 14)
    g.addEdge(76, 80, 18)
    g.addEdge(77, 96, 14)
    g.addEdge(77, 78, 17)
    g.addEdge(77, 95, 13)
    g.addEdge(78, 81, 27)
    g.addEdge(79, 92, 17)
    g.addEdge(79, 93, 20)
    g.addEdge(80, 91, 26)
    g.addEdge(80, 97, 15)
    g.addEdge(80, 96, 8)
    g.addEdge(81, 82, 18)
    g.addEdge(82, 98, 48)
    g.addEdge(83, 84, 15)
    g.addEdge(84, 87, 18)
    g.addEdge(85, 86, 8)
    g.addEdge(86, 87, 9)
    g.addEdge(87, 88, 30)
    g.addEdge(91, 92, 18)
    g.addEdge(93, 94, 9)
    g.addEdge(94, 95, 35)
    g.addEdge(96, 97, 10)
    g.addEdge(98, 99, 33)

    inicial = 1

    print('Digite o numero do vertice inicial: ')

    inicial = int(input())

    if inicial > 0 and inicial < 101:
        for i in range(1, len(g.nodes) + 2):
            if i != inicial:
                print("Caminho do vertice ", inicial, " até o vertice ", i, ": ",
                      shortest_path(g, inicial, i))
            else:
                print('Cidade não encontrada')
