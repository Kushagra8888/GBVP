__author__ = 'kushasharma'
from collections import deque

class linear_tree:
    def __init__(self, start_vertex, gbvp_graph):
        self.edges = set()
        max_weight_eddge_vertex = gbvp_graph.get_max_weight_edge_vertex(start_vertex)
        self.vertices = deque([start_vertex, max_weight_eddge_vertex])
        self.lower_end = start_vertex
        self.higher_end = max_weight_eddge_vertex
        self.primitive_cycle = False
        self.primitive_cycle_at_higher = True
        self.gbvp_graph = gbvp_graph

    def max_edge_at_lower_end(self):
        return self.gbvp_graph.get_max_weight_edge_vertex(self.lower_end, self.vertices[1])

    def max_edge_at_higher_end(self):
        return self.gbvp_graph.get_max_weight_edge_vertex(self.higher_end, self.vertices[len(self.vertices) - 2])

    def check_for_primitive_cycle(self, vertex, higher = True):
        if higher:
            for idx in xrange(len(self.vertices) - 1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True
        else:
            for idx in xrange(len(self.vertices) - 1, 0, -1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True
                    self.primitive_cycle_at_higher = False

    def extend(self):
        max_at_higher = self.max_edge_at_higher_end()
        max_at_lower = self.max_edge_at_lower_end()
        if max_at_higher == max_at_lower == 0:
            return False
        if max_at_higher > max_at_lower:
            self.vertices.append(max_at_higher)
            self.check_for_primitive_cycle(max_at_higher)
        else:
            self.vertices.appendleft(max_at_lower)
            self.check_for_primitive_cycle(max_at_lower, False)
        return True