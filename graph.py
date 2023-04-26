class Graph:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.adj = {}
        self._h = {}

    # para debugeo
    def __str__(self) -> str:
        text = f'{self.start} -> {self.end}\n'
        for key, value in self.adj.items():
            text += key + ": " + str(value) + " h=" + str(self._h[key]) + "\n"
        return text

    def push(self, n1, n2, c: int) -> None:
        if n1 not in self.adj:
            self.adj[n1] = []
        self.adj[n1].append((n2, c))

    def add(self, node, value = 0) -> None:
        self.adj[node] = []
        self._h[node] = value

    def dfs(self):
        def search(self, node, visited):
            if self.end in visited:
                return
            visited.append(node)
            for n, _ in self.adj[node]:
                if n not in visited:
                    search(self, n, visited)

        visited = []
        search(self, self.start, visited)
        cost = 0
        for i in range(len(visited) - 1):
            for x, c in self.adj[visited[i]]:
                if x == visited[i+1]:
                    cost += c
                    break
        return visited, cost

    def uniformCost(self):
        pass

    def greedy(self):
        pass

    def Astar(self):
        pass
