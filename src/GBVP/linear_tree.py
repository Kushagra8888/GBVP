__author__ = 'kushasharma'
from collections import deque

class linear_tree:
    def __init__(self, start_vertex, gbvp_graph):
        self.edges = set()
        self.gbvp_graph = gbvp_graph
        max_weight_edge_vertex = self.gbvp_graph.get_max_weight_edge_vertex(start_vertex, set())
        if max_weight_edge_vertex > 0:
            self.vertices = deque([start_vertex, max_weight_edge_vertex])
            self.lower_end = start_vertex
            self.higher_end = max_weight_edge_vertex
            self.primitive_cycle = False
            self.is_primitive_cycle_at_higher = True
        else:
            self.vertices = deque([start_vertex])
            self.lower_end = start_vertex
            self.higher_end = start_vertex
            self.primitive_cycle = False
            self.is_primitive_cycle_at_higher = True


    def max_edge_at_lower_end(self):
        return self.gbvp_graph.get_max_weight_edge_vertex(self.lower_end, {self.vertices[1]})

    def max_edge_at_higher_end(self):
        return self.gbvp_graph.get_max_weight_edge_vertex(self.higher_end, {self.vertices[len(self.vertices) - 2]})

    def check_for_primitive_cycle(self, vertex, higher = True):
        if higher:
            for idx in xrange(len(self.vertices) - 1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True
        else:
            for idx in xrange(len(self.vertices) - 1, 0, -1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True
                    self.is_primitive_cycle_at_higher = False

    def extend(self):
        if len(self.vertices) == 1:
            return False
        max_at_higher = self.max_edge_at_higher_end()
        max_weight_at_higher = self.gbvp_graph.weight(self.higher_end, max_at_higher)
        max_at_lower = self.max_edge_at_lower_end()
        max_weight_at_lower = self.gbvp_graph.weight(self.lower_end, max_at_lower)
        if max_weight_at_higher == max_weight_at_lower == 0:
            return False
        elif max_weight_at_higher > max_weight_at_lower:
            self.vertices.append(max_at_higher)
            self.higher_end = max_at_higher
            self.check_for_primitive_cycle(max_at_higher)
        else:
            self.vertices.appendleft(max_at_lower)
            self.lower_end = max_at_lower
            self.check_for_primitive_cycle(max_at_lower, False)
        return True