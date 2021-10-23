def bfs(graph, root_vertex, vertexes_list):
    # Initialize the state for every vertex in a graph
    for vertex in vertexes_list:
        is_discovered[vertex] = 0
        predecessors[vertex] = None
        distance_to_root[vertex] = None
        color_vertexes[vertex] = None

    # Create a list to store visited vertexes.
    # Create a list to store queue vertexes.
    vertexes_queue = []

    # Add the root vertex to queue
    vertexes_queue.append(root_vertex)
    # Change the status of the root vertex to discovered, we use 0 and 1
    # to represent the state of vertex. O == undiscovered and is 1 == discovered
    is_discovered[root_vertex] = 1

    # Change the color_vertexes of the root vertex
    color_vertexes[root_vertex] = "red"
    distance_to_root[root_vertex] = 0

    while vertexes_queue:
        vertex = vertexes_queue.pop(0)
        print("the node that is being processed: {}".format(vertex))

        for neighbour in graph[vertex]:
            if is_discovered[neighbour] == 0:
                is_discovered[neighbour] = 1
                distance_to_root[neighbour] = distance_to_root[vertex] + 1
                if color_vertexes[vertex] == "blue":
                    color_vertexes[neighbour] = "red"
                else:
                    color_vertexes[neighbour] = "blue"
                predecessors[neighbour] = vertex
                vertexes_queue.append(neighbour)
            elif distance_to_root[neighbour] == distance_to_root[vertex]:
                global odd_cycle
                global bipartite
                odd_cycle = True
                bipartite = False
                return lowest_common_ancestor(vertex, neighbour)

    bipartite = True
    return color_vertexes


# Function lowest common ancestor is used to find the common ancestor of
# two vertexes (that have the same depth and are connected.
def lowest_common_ancestor(ancestor, neighbour):
    while ancestor != neighbour:
        # odd_cycle_vertexes is used just to store the vertexes of the cycle
        odd_cycle_vertexes[distance_to_root[ancestor]] = {ancestor, neighbour}
        ancestor = predecessors[ancestor]
        neighbour = predecessors[neighbour]

    odd_cycle_vertexes[distance_to_root[ancestor]] = {ancestor, neighbour}
    return odd_cycle_vertexes


def check_bfs_result(bfs_result_value, odd_cycle_value, bipartite_value, graph, vertexes_list):
    # Check if the odd cycle value is true, is so print the bfs graph result.
    # In this case the odd cycle is going to be printed.
    if odd_cycle_value is True:
        print("An odd cycle is identified")
        print(bfs_result_value)

    # Check if the bipartite_value is true, and then print the result of the bfs function.
    # In this case the nodes colored with be printed
    elif bipartite_value is True:
        print("Graph is bipartite")
        print(bfs_result_value)
        print("-------")
        # Check it there are ni vertex that is disconnected from the graph, if so rerun the function into that
        # part.
        print("Checking for disconnection:")
        while check_for_none(color_vertexes):
            disconnected_vertex = []
            for key, value in color_vertexes.items():
                if value is not None:
                    del graph[key]
                elif value is None:
                    disconnected_vertex.append(key)
                    print("Vertex: {} is disconnected.".format(key))
                    print(disconnected_vertex)
            color_vertexes.clear()
            if len(disconnected_vertex) != 0:
                disconnected_vertex.pop(0)
                print(bfs(graph, disconnected_vertex[0], vertexes_list))


def check_for_none(vertexes):
    for key, value in vertexes.items():
        if value is None:
            return True


# while check(my_list):
#     for item in my_list:
#         if condition:
#             item[2] = 1
#         else:
#             do_sth()
if __name__ == '__main__':
    print("Graph 1:")
    is_discovered = {}
    predecessors = {}
    distance_to_root = {}
    color_vertexes = {}
    odd_cycle_vertexes = {}
    global odd_cycle
    global bipartite

    graph_1 = {'A': {'B', 'G'},
               'B': {'A', 'C', 'F'},
               'C': {'B', 'E', 'D'},
               'D': {'C', 'G', 'H'},
               'E': {'C'},
               'F': {'B'},
               'G': {'A', 'D'},
               'H': {'D'}}

    # call bfs function and check the result of it.
    check_bfs_result(bfs(graph_1, "A", graph_1.keys()), odd_cycle, bipartite, graph_1, graph_1.keys())

    print("\n----------------------------------------")
    print("Graph 2:")
    # Clean all dictionaries, to implement new case.
    is_discovered.clear()
    predecessors.clear()
    distance_to_root.clear()
    color_vertexes.clear()
    odd_cycle_vertexes.clear()
    odd_cycle = False
    bipartite = False

    graph_2 = {
        'A': {'G', 'E'},
        'B': {'D'},
        'C': {'F', 'G'},
        'E': {'A'},
        'F': {'C'},
        'G': {'A', 'C'},
        'D': {'B'}
    }
    # Call bfs function and check the result of it.
    check_bfs_result(bfs(graph_2, "A", graph_2.keys()), odd_cycle, bipartite, graph_2, graph_2.keys())

    print("\n----------------------------------------")
    print("Graph 3:")

    # Clean all dictionaries, to implement new case.
    is_discovered.clear()
    predecessors.clear()
    distance_to_root.clear()
    color_vertexes.clear()
    odd_cycle_vertexes.clear()
    odd_cycle = False
    bipartite = False

    graph_3 = {'A': {'B', 'C', 'D', 'E', 'F', 'G'},
               'B': {'A', 'F', 'C', 'D'},
               'C': {'A', 'B', 'E', 'D', 'G'},
               'D': {'C', 'A', 'B', 'E', 'G'},
               'E': {'G', 'D', 'C', 'A', 'F'},
               'F': {'A', 'B', 'E', 'G'},
               'G': {'A', 'F', 'E', 'D', 'C'},
               'H': {'D'}}
    # Call bfs function and check the result of it.
    check_bfs_result(bfs(graph_3, "A", graph_3.keys()), odd_cycle, bipartite, graph_3, graph_3.keys())
