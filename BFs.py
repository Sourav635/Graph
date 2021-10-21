from collections import deque


class Graph():

    def __init__(self, n):
        self.nodes = n
        self.adj_list = {}

        for x in n:
            self.adj_list[x] = []

    def add_edges(self, edges):

        for x in edges:
            self.adj_list[x[0]].append(x[1])
            self.adj_list[x[1]].append(x[0])

    def disp_list(self):
        print(self.adj_list)

    def bfs(self):

        temp_q = deque()
        temp_q.append(self.nodes[0])
        visited = []

        while temp_q:

            a = temp_q.popleft()
            print(a, end=" ")

            for x in self.adj_list[a]:
                if x not in visited and x not in temp_q:
                    temp_q.append(x)

            visited.append(a)


nodes = ["A", "B", "C", "D", "E", "F"]
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "E"), ("B", "F"), ("C", "F")]

# nodes = [1, 2, 3, 4, 5, 6]
# edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)]

# nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9), (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]

nodes = [1, 2, 3, 4]
edges = [(1, 2), (1, 3), (2, 4), (2, 3)]

obj_1 = Graph(nodes)
obj_1.add_edges(edges)


obj_1.bfs()
