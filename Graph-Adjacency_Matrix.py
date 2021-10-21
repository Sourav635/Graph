class Graph():

    def __init__(self, n):
        self.nodes = n
        self.graph = [[0]*n for i in range(n)]

    def display(self):
        for i in range(self.nodes):
            print(self.graph[i])
        print()

    def add_edge(self, start, end):
        self.graph[start][end] = 1
        self.graph[end][start] = 1

    def check_edge(self, start, end):
        if start in range(self.nodes) and end in range(self.nodes):
            [print("Edge exists") if self.graph[start][end] == 1 else print("Edge doesn't exists")]
        else:
            print("Node doesn't exist")


obj = Graph(4)
obj.display()

obj.add_edge(0, 1)
obj.add_edge(0, 2)
obj.add_edge(0, 3)
obj.add_edge(1, 2)


obj.display()
# obj.check_edge(0, 5)
obj.check_edge(0, 1)
obj.check_edge(0, 0)
