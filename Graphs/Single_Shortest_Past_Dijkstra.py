class Graph:
    def __init__(self, num):
        self.graph = [[0 for _ in range(num)] for _ in range(num)]

    def add_edge_undirect(self, from_vertex: int, to_vertex: int, weight: int):
        if from_vertex == to_vertex:
            print(f"Error: {from_vertex} and {to_vertex} are equal")
            return

        self.graph[from_vertex][to_vertex] = weight
        self.graph[to_vertex][from_vertex] = weight

    def dijkstra(self, src_vertex: int):
        dist = [float('inf')] * len(self.graph)
        dist[src_vertex] = 0
        visited = [False] * len(self.graph)
        previous = [None] * len(self.graph)

        def find_closest() -> int:
            min_weight = float('inf')
            min_index = None
            for vertex in range(len(self.graph)):
                if dist[vertex] < min_weight and not visited[vertex]:
                    min_weight = dist[vertex]
                    min_index = vertex

            return min_index

        for _ in range(len(self.graph)):
            closest = find_closest()

            visited[closest] = True

            for v in range(len(self.graph)):
                if self.graph[closest][v] > 0 and not visited[v] and dist[v] > dist[closest] + self.graph[closest][v]:
                    dist[v] = dist[closest] + self.graph[closest][v]
                    previous[v] = closest

        return previous


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge_undirect(0, 1, 6)
    g.add_edge_undirect(0, 3, 1)
    g.add_edge_undirect(1, 3, 2)
    g.add_edge_undirect(3, 4, 1)
    g.add_edge_undirect(1, 4, 2)
    g.add_edge_undirect(1, 2, 5)
    g.add_edge_undirect(4, 2, 5)

    print(g.dijkstra(0))
