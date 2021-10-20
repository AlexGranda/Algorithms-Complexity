class Vertex:
    def __init__(self, status, distance_to_root, predecessors):
        self.status = status
        self.distance_to_root = distance_to_root
        self.predecessors = predecessors


def bfs(graph, vertexes_list):

    object_vertexes_list = []
    for i in graph:
        object_vertex = Vertex(0, None, None)
        object_vertexes_list.append(object_vertex)
        print(object_vertex.status)


if __name__ == '__main__':
    graph_a = {'A': {'B', 'G'},
             'B': {'A', 'C', 'F'},
             'C': {'B', 'I', 'D'},
             'D': {'C', 'G', 'H'},
             'E': {'C'},
             'F': {'B'},
             'G': {'A', 'D'},
             'H': {'D'}}
