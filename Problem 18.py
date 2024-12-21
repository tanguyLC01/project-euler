triangle = [[75], [95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94 ,29],
[53, 71, 44, 65, 25, 43, 91, 52, 97 ,51 ,14],
[70, 11, 33, 28, 77, 73, 17, 78, 39 ,68 ,17 ,57],
[91, 71, 52, 38, 17, 14, 91, 43, 58 ,50 ,27 ,29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73 ,16 ,69 ,87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73 ,93 ,38 ,53, 60, 4, 23]]

class Node:

    def __init__(self, i, j, value):
        self.position = (i, j)
        self.value = value
        self.children = []

    def add_children(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.value)

class Graph:

    def __init__(self, values):
        self.floors = [[Node(0, 0, values[0][0])]]
        for i in range(1, len(values)):
            self.floors.append([])
            for j in range(len(values[i])):
                if j == 0:
                    self.floors[i].append(Node(i, j, values[i][j]))
                    self.floors[i-1][j].add_children(self.floors[i][j])
                elif j == (len(values[i]) - 1):
                    self.floors[i].append(Node(i, j, values[i][j]))
                    self.floors[i-1][j-1].add_children(self.floors[i][j])
                else:
                    self.floors[i].append(Node(i, j, values[i][j]))
                    self.floors[i-1][j-1].add_children(self.floors[i][j])
                    self.floors[i-1][j].add_children(self.floors[i][j])
        self.longueur = len(self.floors)

    def __repr__(self):
        res = ""
        for i in range(len(self.floors)):
            for j in range(len(self.floors[i])):
                res +=  str(self.floors[i][j])
                res += " "
            res += "\n"
        return res
           

    def all_paths(self, index_node, paths):
        active_node = self.floors[index_node[0]][index_node[1]]
        return [[active_node, elem for elem in all_paths()]]

g = Graph(triangle)
print(g)
print("\n")
paths = []
g.all_paths((12, 2), paths)
print(paths)
#res = 0
#for i in range(len(paths)):
#   path = list(map(lambda x: x.value, paths[i]))
#   print(path)



