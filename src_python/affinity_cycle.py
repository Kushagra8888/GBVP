__author__ = 'kushasharma'
from edge import edge

class affinity_cycle:
    def __init__(self, vertex_list, gbvp_graph, higher = True):
        self.edges = set([])
        self.gbvp_graph = gbvp_graph
        if higher:
            self.cycle_node = vertex_list[-1]
            self.moving_end = vertex_list[-2]
            start_idx = len(vertex_list) - 1
            idx = start_idx
            while(idx == start_idx or vertex_list[idx] != self.cycle_node):
                self.edges.add(edge(vertex_list[idx], vertex_list[idx - 1]))
                idx -= 1
            self.fixed_end = vertex_list[idx + 1]
        else:
            self.cycle_node = vertex_list[0]
            self.moving_end = vertex_list[1]
            start_idx = 0
            idx = start_idx
            while(idx == start_idx or vertex_list[idx] != self.cycle_node):
                self.edges.add(edge(vertex_list[idx], vertex_list[idx + 1]))
                idx += 1
            self.fixed_end = vertex_list[idx - 1]

    def is_extension_possible(self, new_edge, cycle_completing_edge):
        return max(new_edge.weight, cycle_completing_edge.weight) > min(map(lambda x: x.weight , self.edges))

    def extend(self):
        new_vertex = self.gbvp_graph.get_max_weight_edge_vertex_for_extension(self.cycle_node, self.moving_end,
                                                                         self.fixed_end)
        new_edge = edge(new_vertex, self.moving_end)
        cycle_completing_edge = edge(new_vertex, self.cycle_node)
        if self.is_extension_possible(new_edge, cycle_completing_edge):
            self.edges.remove(edge(self.cycle_node, self.moving_end))
            self.add(new_edge, cycle_completing_edge)
            return True
        else:
            return False

    def __str__(self):
        return "\nAffinity Cycle: " + "\nCycle Node: " + str(self.cycle_node) + "\nOther Node: " + str(self.moving_end)\
               + "\nEdges: " + str(self.edges)