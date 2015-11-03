__author__ = 'kushasharma'
from edge import edge

class affinity_cycle:
    def __init__(self, vertex_list, gbvp_graph, higher = True):
        self.edges = set([])
        self.gbvp_graph = gbvp_graph
        self.all_cycle_nodes = set()
        if higher:
            self.cycle_node = vertex_list[-1]
            self.moving_end = vertex_list[-2]
            start_idx = len(vertex_list) - 1
            idx = start_idx
            while idx == start_idx or vertex_list[idx] != self.cycle_node:
                self.all_cycle_nodes.add(vertex_list[idx])
                self.edges.add(edge(vertex_list[idx], vertex_list[idx - 1], self.gbvp_graph))
                idx -= 1
            self.fixed_end = vertex_list[idx + 1]

        else:
            self.cycle_node = vertex_list[0]
            self.moving_end = vertex_list[1]
            start_idx = 0
            idx = start_idx
            while idx == start_idx or vertex_list[idx] != self.cycle_node:
                self.all_cycle_nodes.add(vertex_list[idx])
                self.edges.add(edge(vertex_list[idx], vertex_list[idx + 1], self.gbvp_graph))
                idx += 1
            self.fixed_end = vertex_list[idx - 1]

    def is_extension_possible(self, new_edge, cycle_completing_edge):
        return max(new_edge.weight, cycle_completing_edge.weight) >= min(map(lambda x: x.weight , self.edges))

    def switch_cycle_node(self):
        self.cycle_node, self.moving_end = self.moving_end = self.cycle_node

    def extend(self):
        new_vertex = self.gbvp_graph.get_max_weight_edge_vertex(self.cycle_node, self.all_cycle_nodes)
        if new_vertex < 0:
            return False
        new_edge = edge(new_vertex, self.moving_end, self.gbvp_graph)
        cycle_completing_edge = edge(new_vertex, self.cycle_node, self.gbvp_graph)
        if self.is_extension_possible(new_edge, cycle_completing_edge):
            self.edges.remove(edge(self.cycle_node, self.moving_end, self.gbvp_graph))
            self.edges.update([new_edge, cycle_completing_edge])
            self.moving_end = new_vertex
            self.all_cycle_nodes.add(new_vertex)
            return True
        else:
            return False

    def __str__(self):
        return "\nAffinity Cycle: " + "\nCycle Node: " + str(self.cycle_node) + "\nOther Node: " + str(self.moving_end)\
               + "\nEdges: " + str(self.edges)