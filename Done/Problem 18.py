import numpy as np

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

test_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_children(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.value)

class Graph:

    def __init__(self, values):
        self.root = Node(values[0][0])
        self.generate_graph_from_root(self.root, values[1:])
    
    def generate_graph_from_root(self, root, values):
        parents = [root]
        new_parents = []
        for i in range(len(values)):
            for j in range(len(values[i])):
                n = Node(values[i][j])
                if j == 0:
                    parents[0].add_children(n)
                elif j == len(values[i]) - 1:
                    parents[-1].add_children(n)
                else:
                    parents[j].add_children(n)
                    parents[j-1].add_children(n)
                new_parents.append(n)
            parents = new_parents
            new_parents = []

    def __repr__(self):
        return self.root.__str__()
           


def max_path_sum(root):
    
    max_cost = -np.inf
    max_path = []
    
    def dfs(node, current_path, cost):
        nonlocal max_cost, max_path
        
        current_path.append(node)
        if node.children == []:
            max_cost = max(max_cost, cost)
            if max_cost == cost:
                max_path = current_path
        for child in node.children:
            dfs(child, current_path, cost + child.value)
        
        current_path.pop()
    
    dfs(root, [], root.value)
    return max_cost, max_path

print(max_path_sum(Graph(triangle).root))
#for i in range(len(paths)):
#   path = list(map(lambda x: x.value, paths[i]))
#   print(path)



