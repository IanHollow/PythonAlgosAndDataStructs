class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph.setdefault(node)

    def add_edge(self, node1, node2):
        node = Node(node1)
        node.next = self.graph[node2]
        self.graph[node2] = node

        node = Node(node2)
        node.next = self.graph[node1]
        self.graph[node1] = node

    def search_DFS_recur(self):
        pass

    def search_DFS_iter(self):
        pass

    def search_BFS(self):
        pass

    def print_graph(self):
        arrow = "->"
        linked_list = ""
        for key in self.graph:
            current_node = self.graph[key]
            while current_node is not None:
                linked_list += f" {arrow} {current_node.data}"
                current_node = current_node.next
            print(f"({key}){linked_list}")
            linked_list = ""


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)

    graph.add_edge(1, 6)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 3)
    graph.add_edge(6, 3)

    graph.print_graph()
