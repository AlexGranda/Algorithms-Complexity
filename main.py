import collections

is_discovered = []
predecessors = []
distance_to_root = []
color = []


def bfs(graph, root_vertex, vertexes_list):
    object_vertexes_list = []

    # Initialize the data structures.
    distance = 0
    for vertex in vertexes_list:
        is_discovered[vertex] = 0
        predecessors[vertex] = None
        distance_to_root[vertex] = None
        color[vertex] = None


    # Create a list to store visited vertexes.
    # Create a list to store queue vertexes.
    vertexes_visited = []
    vertexes_queue = []

    # Add the root vertex to queue
    vertexes_queue.append(root_vertex)
    # Change the status of the root vertex to discovered, we use 0 and 1
    # to represent the state of vertex. O == undiscovered and is 1 == discovered
    is_discovered[root_vertex] = 1

    # Change the color of the root vertex
    color[root_vertex] = "red"
    distance_to_root[root_vertex] = 0

    while vertexes_queue:
        vertex = vertexes_queue.pop(0)
        print("the node that is being processed: {}".format(vertex))

        for neighbour in graph[vertex]:
            if is_discovered[neighbour] == 0:
                is_discovered[neighbour] = 1
                distance_to_root[neighbour] = distance_to_root[vertex] + 1
                if color[vertex] == "blue":
                    color[neighbour] = "red"
                else:
                    color[neighbour] = "blue"
                predecessors[neighbour] = vertex
                vertexes_queue.append(neighbour)
            else:
                if distance_to_root[neighbour] == distance_to_root[vertex]:
                    print("test")


# def bfs(visit_complete, graph, current_node):
#     visit_complete.append(current_node)
#     queue = []
#     queue.append(current_node)
#
#     while queue:
#         s = queue.pop(0)
#         print(s)
#
#         for neighbour in graph[s]:
#             if neighbour not in visit_complete:
#                 visit_complete.append(neighbour)
#                 queue.append(neighbour)
#
#
# bfs([], graph, 'A')


if __name__ == '__main__':
    graph_a = {'A': {'B', 'G'},
               'B': {'A', 'C', 'F'},
               'C': {'B', 'I', 'D'},
               'D': {'C', 'G', 'H'},
               'E': {'C'},
               'F': {'B'},
               'G': {'A', 'D'},
               'H': {'D'}}

    # Case: A is the root of graph
    for i in graph_a:
        print(graph_a[i])
    # bfs(graph_a, 0, graph_a.keys())

