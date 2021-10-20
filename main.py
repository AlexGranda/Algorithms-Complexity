class Vertex:
    def __init__(self, is_discovered, distance_to_root, predecessors):
        self.is_discovered = is_discovered
        self.distance_to_root = distance_to_root
        self.predecessors = predecessors
        self.color = None


def bfs(graph, vertexes_list):

    object_vertexes_list = []

    #Initialize the data structures
    distance = 0
    for _ in vertexes_list:
        object_vertex = Vertex(False, 0, None)
        object_vertexes_list.append(object_vertex)
        print(object_vertex.is_discovered)

    #Initial set ups
    object_vertexes_list[0].color = "red"
    queue = [object_vertexes_list[0]]

    for vertex in object_vertexes_list:
        if not vertex.is_discovered:
            vertex.is_discovered = True
            vertex.distance_to_root += 1



if __name__ == '__main__':
    graph_a = {'A': {'B', 'G'},
             'B': {'A', 'C', 'F'},
             'C': {'B', 'I', 'D'},
             'D': {'C', 'G', 'H'},
             'E': {'C'},
             'F': {'B'},
             'G': {'A', 'D'},
             'H': {'D'}}

    bfs(graph_a, graph_a.keys())
