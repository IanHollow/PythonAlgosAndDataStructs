class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, num):
        self.graph = []
        for _ in range(num):
            self.graph.append([0] * num)

    def add_edge_undirect(self, from_vertex, to_vertex):
        if from_vertex == to_vertex:
            print(f"Error: {from_vertex} and {to_vertex} are equal")
            return

        self.graph[from_vertex][to_vertex] = 1
        self.graph[to_vertex][from_vertex] = 1

    def dfs_search_iter(self, start_vertex) -> list:
        stack = [start_vertex]
        visited = [False] * len(self.graph)
        dfs_result = []

        for _ in self.graph:
            while stack and visited[stack[-1]]:
                stack.pop()

            if not stack:
                return dfs_result

            start_vertex = stack.pop()
            visited[start_vertex] = True
            dfs_result.append(start_vertex)

            for i in range(len(self.graph[start_vertex])):
                if not visited[i] and self.graph[start_vertex][i]:
                    stack.append(i)

        return dfs_result

    def dfs_search_recur(self, start_vertex) -> list:
        visited = [False] * len(self.graph)
        dfs_result = []

        def dfs(start_vertex):

            visited[start_vertex] = True
            dfs_result.append(start_vertex)

            for i in range(len(self.graph)):
                if not visited[i] and self.graph[start_vertex][i]:
                    dfs(i)

        dfs(start_vertex)

        return dfs_result

    def bfs_search(self, start_vertex) -> list:
        queue = Node(start_vertex)
        tail = queue
        visited = [False] * len(self.graph)
        bfs_result = []

        while queue is not None:
            while queue is not None and visited[queue.data]:
                queue = queue.next

            if queue is None:
                print("exit")
                return bfs_result

            visited[queue.data] = True
            bfs_result.append(queue.data)

            for i in range(len(self.graph[queue.data])):
                if not visited[i] and self.graph[queue.data][i]:
                    tail.next = Node(i)
                    tail = tail.next
            queue = queue.next

        return bfs_result

    def printGraph(self):
        first_str = "   "
        for i in range(len(self.graph)):
            first_str += f"{i}  "
        print(first_str)
        for i, arr in enumerate(self.graph):
            print(f"{i} {arr}")


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge_undirect(0, 1)
    g.add_edge_undirect(0, 2)
    g.add_edge_undirect(1, 2)
    g.add_edge_undirect(0, 3)

    g.printGraph()

    print(g.dfs_search_iter(1))
    print(g.dfs_search_recur(1))
    print(g.bfs_search(1))
