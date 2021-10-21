class Graph():

    def __init__(self, n):
        self.nodes = n
        self.adj_list = {}
        for x in self.nodes:
            self.adj_list[x] = []

    def add_edges(self, edges):
        for x in edges:
            self.adj_list[x[0]].append(x[1])
            self.adj_list[x[1]].append(x[0])

    def disp_adj(self):
        print(self.adj_list)

    def dfs(self):

        stack = []
        stack.append(self.nodes[0])
        visited = []
        ans = []
        while stack:

            if stack[-1] not in ans:
                ans.append(stack[-1])
            visited.append(stack[-1])

            for x in self.adj_list[stack[-1]]:
                if x not in visited and x not in stack:
                    stack.append(x)
                    break
            else:
                stack.pop()
            # print(stack)
        print(*ans)


nodes = [0, 1, 2, 3, 4, 5, 6]
edges = [(0, 1), (0, 3), (1, 3), (1, 2), (1, 5), (1, 6), (2, 3), (2, 4), (2, 6), (3, 4), (4, 5)]

obj = Graph(nodes)
obj.add_edges(edges)
obj.dfs()
# obj.disp_adj()
