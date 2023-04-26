class Graph:
    def __init__(self):
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

    def push(self, n1, n2, c):
        if n1 not in self.adj:
            self.adj[n1] = []
        self.adj[n1].append((n2, c))

    def h(self, node, value):
        self._h[node] = value

    def goal(self, start, end):
        if start not in self.adj:
            self.adj[start] = []
        self.start = start
        if end not in self.adj:
            self.adj[end] = []
        self.end = end

    def dfs():
        pass

    def uniformCost():
        pass

    def greedy():
        pass

    def Astar():
        pass
