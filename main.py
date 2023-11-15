from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set()
    frontier = set([start_node])
    # print(graph)
    while len(frontier) != 0:
        # print('frontier',str(frontier))
        # print(str(result))
        here = frontier.pop()
        # print(visited)
        if here in result:
            # print('already visited ',here)
            continue
        else:
            result.add(here)
            # print('po')
            # print('visited',result)
            # frontier.add(graph[here])
            # k = [i for i in graph[here]]
            # print('k:',k)
            for i in graph[here]:
                frontier.add(i)
    return result

graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), 
                               ('D', 'B'), ('X', 'Y')])

# print(reachable(graph, 'B'))

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), 
                                   ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), 
                                   ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']

test_reachable()




def connected(graph):
    # print(graph.keys())[0]
    # print(graph[1][0])
    nodes = sorted([i for i in graph])
    # r = sorted(reachable(graph, nodes[0]))
    # print(r)
    # print(nodes)
    return sorted(reachable(graph, nodes[0])) == nodes

graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
# print(connected(graph))

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), 
                                   ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), 
                                   ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False

test_connected()


def n_components(graph):
    nodes = sorted([i for i in graph])
    reached = []
    num = 0
    while len(nodes) != 0:
        num += 1
        for i in reachable(graph, nodes[0]):
            reached.append(i)
        print(reached)
        nodes = list(filter(lambda x: x not in reached, nodes))
    """
    Returns:
      the number of connected components in an undirected graph
    """
    return num

graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
print(n_components(graph))

