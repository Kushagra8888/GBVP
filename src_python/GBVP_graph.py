__author__ = 'kushasharma'

class GBVP_graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.length = len(adjacency_matrix)

    def get_max_weight_edge_vertex(self, vertex, ignore_vertex = None):
        max_weight, max_weight_edge_vertex = 0, 0
        for other in range(self.length):
            if not other == ignore_vertex and not other == vertex:
                if  self.adjacency_matrix[vertex][other] > max_weight:
                    max_weight = self.adjacency_matrix[vertex][other]
                    max_weight_edge_vertex = other
        return max_weight_edge_vertex

    def get_max_weight_edge_vertex_for_extension(self, pivot_node, moving_end, fixed_end):
        ignore = {pivot_node, moving_end, fixed_end}
        max_weight, max_weight_edge_vertex = 0, 0
        for other in range(self.length):
            if other not in ignore:
                if  self.adjacency_matrix[pivot_node][other] > max_weight:
                    max_weight = self.adjacency_matrix[pivot_node][other]
                    max_weight_edge_vertex = other
        return max_weight_edge_vertex