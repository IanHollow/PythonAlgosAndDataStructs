class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, num: int):
        self.graph = [None] * num

    def add_edge_direct(self, from_vertex: int, to_vertex: int):
        if from_vertex > len(self.graph)-1 or to_vertex > len(self.graph)-1:
            raise IndexError("to_vertex or from_vertex doesn't exist")

        node = AdjNode(to_vertex)
        node.next = self.graph[from_vertex]
        self.graph[from_vertex] = node

    def add_edge_undirect(self, from_vertex: int, to_vertex: int):
        if from_vertex > len(self.graph)-1 or to_vertex > len(self.graph)-1:
            raise IndexError("to_vertex or from_vertex doesn't exist")

        node = AdjNode(to_vertex)
        node.next = self.graph[from_vertex]
        self.graph[from_vertex] = node

        node = AdjNode(from_vertex)
        node.next = self.graph[to_vertex]
        self.graph[to_vertex] = node

    def search_DFS_recur(self, start_vertex: int) -> list:
        visited = [False] * len(self.graph)
        dfs_results = []

        def dfs(start_vertex):
            visited[start_vertex] = True
            dfs_results.append(start_vertex)

            current_node = self.graph[start_vertex]
            while current_node is not None:
                if not visited[current_node.data]:
                    dfs(current_node.data)
                current_node = current_node.next

        for _ in range(len(self.graph)):
            if start_vertex > len(self.graph)-1:
                start_vertex = 0
            if not visited[start_vertex]:
                dfs(start_vertex)
            start_vertex += 1

        return dfs_results

    def search_DFS_iter(self):
        pass

    def search_BFS(self):
        pass

    def print_graph(self):
        for i in range(len(self.graph)):
            current_node = self.graph[i]
            linked_list = ""
            while current_node is not None:
                linked_list += f" -> {current_node.data}"
                current_node = current_node.next
            print(f"({i}){linked_list}")


if __name__ == "__main__":
    graph = Graph(7)

    graph.add_edge_undirect(1, 6)
    graph.add_edge_undirect(1, 3)
    graph.add_edge_undirect(2, 4)
    graph.add_edge_undirect(4, 3)
    graph.add_edge_undirect(6, 3)

    graph.print_graph()

    print(graph.search_DFS_recur(4))
