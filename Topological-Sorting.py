# --> For Topological Sorting graph should be DAG
# --> Directed(every edge should be Directed) & Acyclic(contains 0 cycle)

class Graph():

    def __init__(self, nodes):

        self.nodes = nodes

        self.adj_list = {}
        for x in self.nodes:
            self.adj_list[x] = []

        self.parent = {}
        for x in self.nodes:
            self.parent[x] = [None]
        self.visited = {}
        for x in self.nodes:
            self.visited[x] = [False]
        self.is_cyclic = False

    def add_edges(self, edges):
        for x in edges:
            self.adj_list[x[0]].append(x[1])

    def disp_adj(self):
        for x in self.adj_list:
            print(x, " --> ", self.adj_list[x])

    def check_cycle(self, src):

        self.visited[src] = True

        for adj_node in self.adj_list[src]:
            print(self.visited)
            print(self.parent)
            if self.visited[adj_node] == False:
                self.parent[adj_node] = src
                self.check_cycle(adj_node)

            elif self.parent[src] != adj_node:
                self.is_cyclic = True
                return

    def cyclic(self):
        return self.is_cyclic


nodes = ["A", "B", "C"]
edges = [("A", "B"), ("B", "C"), ("A", "C")]

nodes = [0, 1, 2, 3]
edges = [(0, 1), (1, 2), (2, 3), (0, 3)]

obj = Graph(nodes)
obj.add_edges(edges)
obj.check_cycle(0)

obj.disp_adj()

print(obj.cyclic())
