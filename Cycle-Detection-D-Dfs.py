class Graph():

    def __init__(self, n):
        self.nodes = n
        self.adj_list = {}
        self.visited = [False]*len(n)
        self.parent = [None]*len(n)
        self.is_cyclic = False
        for x in self.nodes:
            self.adj_list[x] = []

    def add_edges(self, edges):
        for x in edges:
            self.adj_list[x[0]].append(x[1])

    def disp_adj(self):
        for x in self.adj_list:
            print(x, " --> ", self.adj_list[x])

    def cycle_detection(self, src):

        self.visited[src] = True

        for x in self.adj_list[src]:
            print(self.visited)
            print(self.parent)
            if self.visited[x] == False:
                self.parent[x] = src
                self.cycle_detection(x)
            elif self.parent[src] != x:
                self.is_cyclic = True
                return

    def cyclic(self):
        return self.is_cyclic


nodes = [x for x in range(1, 13)]
edges = [(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
         (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)]

nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (0, 3), (1, 2), (2, 0), (3, 4)]

nodes = [x for x in range(7)]
edges = [(0, 1), (0, 2), (1, 4), (2, 3), (3, 1), (3, 5), (4, 6), (5, 4), (6, 5)]

nodes = [0, 1, 2, 3]
edges = [(0, 1), (1, 2), (2, 3), (0, 3)]

obj = Graph(nodes)
obj.add_edges(edges)
obj.disp_adj()
obj.cycle_detection(1)
print(obj.cyclic())
