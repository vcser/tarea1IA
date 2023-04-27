from queue import PriorityQueue


class Graph:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.adj = {}
        self._h = {}

    # DEBUG print
    def __str__(self) -> str:
        text = f'{self.start} -> {self.end}\n'
        for key, value in self.adj.items():
            text += key + ": " + str(value) + " h=" + str(self._h[key]) + "\n"
        return text

    def __getitem__(self, key):
        return self.adj[key]

    def push(self, n1, n2, c: int) -> None:
        if n1 not in self.adj:
            self.adj[n1] = []
        self.adj[n1].append((n2, c))

    def add(self, node, value=0) -> None:
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

    def ucs(self):
        q = PriorityQueue()
        q.put((0, self.start))
        visited = set()
        visited.add(self.start)
        parents = {self.start: None}

        while not q.empty():
            priority, node = q.get()

            # nodo final encontrado
            if node == self.end:
                path = [node]
                prev_node = node

                while prev_node != self.start:
                    parent = parents[prev_node]
                    path.append(parent)
                    prev_node = parent

                path.reverse()
                # calcular costo
                cost = 0
                for i in range(len(path) - 1):
                    for x, c in self.adj[path[i]]:
                        if x == path[i+1]:
                            cost += c
                            break
                return path, cost

            for child, cost in self[node]:
                if child not in visited:
                    visited.add(child)
                    parents[child] = node
                    q.put((priority + cost, child))

    def greedy(self):
        pass

    def Astar(self):
        pass
