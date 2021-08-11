from collections import defaultdict


class Graph:

    def __init__(self, vertices):

        self.V = vertices

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, origem, destino, limite, visitados):

        if origem not in visitados:
            visitados.add(origem)

        if origem == destino:
            return True

        if limite <= 0:
            return False

        for i in self.graph[origem]:
            if self.DFS(i, destino, limite - 1, visitados):
                return True
        return False

    def LDFS(self, origem, destino, limite, visitados):

        for i in range(limite):
            if self.DFS(origem, destino, i, visitados):
                return True
        return False


g = Graph(101)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(1, 13)
g.addEdge(1, 3)
g.addEdge(1, 42)
g.addEdge(2, 74)
g.addEdge(2, 6)
g.addEdge(2, 49)
g.addEdge(2, 4)
g.addEdge(3, 42)
g.addEdge(3, 9)
g.addEdge(6, 7)
g.addEdge(6, 8)
g.addEdge(7, 49)
g.addEdge(7, 14)
g.addEdge(7, 8)
g.addEdge(7, 15)
g.addEdge(8, 16)
g.addEdge(8, 9)
g.addEdge(9, 45)
g.addEdge(9, 19)
g.addEdge(9, 23)
g.addEdge(9, 10)
g.addEdge(10, 46)
g.addEdge(10, 32)
g.addEdge(11, 39)
g.addEdge(11, 12)
g.addEdge(11, 44)
g.addEdge(12, 44)
g.addEdge(12, 26)
g.addEdge(13, 11)
g.addEdge(14, 86)
g.addEdge(14, 28)
g.addEdge(15, 85)
g.addEdge(15, 71)
g.addEdge(16, 17)
g.addEdge(16, 28)
g.addEdge(16, 33)
g.addEdge(17, 18)
g.addEdge(17, 45)
g.addEdge(18, 19)
g.addEdge(18, 23)
g.addEdge(18, 45)
g.addEdge(19, 61)
g.addEdge(20, 21)
g.addEdge(21, 22)
g.addEdge(21, 23)
g.addEdge(22, 25)
g.addEdge(22, 48)
g.addEdge(24, 27)
g.addEdge(25, 33)
g.addEdge(25, 38)
g.addEdge(25, 37)
g.addEdge(26, 43)
g.addEdge(26, 29)
g.addEdge(26, 47)
g.addEdge(27, 34)
g.addEdge(27, 99)
g.addEdge(27, 61)
g.addEdge(28, 38)
g.addEdge(28, 59)
g.addEdge(29, 51)
g.addEdge(29, 41)
g.addEdge(30, 40)
g.addEdge(30, 34)
g.addEdge(32, 46)
g.addEdge(34, 50)
g.addEdge(35, 48)
g.addEdge(35, 56)
g.addEdge(36, 89)
g.addEdge(36, 39)
g.addEdge(36, 41)
g.addEdge(37, 38)
g.addEdge(37, 55)
g.addEdge(37, 48)
g.addEdge(38, 58)
g.addEdge(40, 43)
g.addEdge(40, 50)
g.addEdge(41, 100)
g.addEdge(41, 53)
g.addEdge(43, 47)
g.addEdge(48, 60)
g.addEdge(51, 52)
g.addEdge(52, 66)
g.addEdge(52, 63)
g.addEdge(52, 78)
g.addEdge(53, 62)
g.addEdge(53, 89)
g.addEdge(54, 73)
g.addEdge(54, 57)
g.addEdge(54, 62)
g.addEdge(54, 74)
g.addEdge(55, 58)
g.addEdge(55, 70)
g.addEdge(56, 64)
g.addEdge(56, 65)
g.addEdge(57, 74)
g.addEdge(59, 83)
g.addEdge(60, 61)
g.addEdge(61, 99)
g.addEdge(62, 89)
g.addEdge(63, 82)
g.addEdge(65, 70)
g.addEdge(66, 95)
g.addEdge(66, 94)
g.addEdge(67, 68)
g.addEdge(67, 100)
g.addEdge(67, 75)
g.addEdge(68, 100)
g.addEdge(68, 69)
g.addEdge(69, 75)
g.addEdge(69, 79)
g.addEdge(69, 72)
g.addEdge(71, 74)
g.addEdge(72, 90)
g.addEdge(73, 90)
g.addEdge(75, 93)
g.addEdge(75, 94)
g.addEdge(76, 94)
g.addEdge(76, 92)
g.addEdge(76, 80)
g.addEdge(77, 96)
g.addEdge(77, 78)
g.addEdge(77, 95)
g.addEdge(78, 81)
g.addEdge(79, 92)
g.addEdge(79, 93)
g.addEdge(80, 91)
g.addEdge(80, 97)
g.addEdge(80, 96)
g.addEdge(81, 82)
g.addEdge(82, 98)
g.addEdge(83, 84)
g.addEdge(84, 87)
g.addEdge(85, 86)
g.addEdge(86, 87)
g.addEdge(87, 88)
g.addEdge(91, 92)
g.addEdge(93, 94)
g.addEdge(94, 95)
g.addEdge(96, 97)
g.addEdge(98, 99)

origem = 0
destino = 11
limite = 3

visitados = set()

if g.LDFS(origem, destino, limite, visitados):
    print("O destino foi encontrado!")
    print(visitados)
else:
    print("O destino não foi encontrado!")