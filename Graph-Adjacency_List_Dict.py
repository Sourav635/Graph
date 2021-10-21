class Graph():

    def __init__(self, n):
        self.nodes = n
        self.adj_list = {}

        for x in self.nodes:
            self.adj_list[x] = set()

    def display(self):
        for x in self.adj_list:
            print(x, " --> ", self.adj_list[x])
        print()

    def add_edge(self, start, end):
        self.adj_list[start].add(end)
        self.adj_list[end].add(start)


nodes = [0, 1, 2, 3]
all_edges = [(0, 1), (0, 2), (0, 3), (1, 2)]

obj = Graph(nodes)
obj.display()

for x in all_edges:
    obj.add_edge(x[0], x[1])

obj.display()
