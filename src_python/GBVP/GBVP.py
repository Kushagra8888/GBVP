__author__ = 'kushasharma'
from GBVP_graph import GBVP_graph
from linear_tree import linear_tree
from affinity_cycle import affinity_cycle



def get_components(adjacency_matrix):
    gbvp_graph = GBVP_graph(adjacency_matrix)
    components = []
    remaining_nodes = set(range(gbvp_graph.length))
    while remaining_nodes:
        start_vertex = remaining_nodes.pop()
        remaining_nodes.add(start_vertex)
        tree = linear_tree(start_vertex, gbvp_graph)
        while not tree.primitive_cycle:
            if not tree.extend():
                break
        if tree.primitive_cycle:
            an_affinity_cycle = affinity_cycle(tree.vertices, gbvp_graph, tree.is_primitive_cycle_at_higher)
            while an_affinity_cycle.extend():
                pass
            remove_vertices = an_affinity_cycle.all_cycle_nodes
        else:
            remove_vertices = set(linear_tree.vertices)
        remaining_nodes.difference_update(remove_vertices)
        components.append(remove_vertices)
        gbvp_graph.cut_component(remove_vertices)
    return components


