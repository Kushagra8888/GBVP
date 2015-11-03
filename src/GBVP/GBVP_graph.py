__author__ = 'kushasharma'

class GBVP_graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.length = len(adjacency_matrix)
        
    def weight(self, v1, v2):
        return self.adjacency_matrix[v1][v2]

    def get_max_weight_edge_vertex(self, vertex, ignore):
        ignore.add(vertex)
        max_weight, max_weight_edge_vertex = -1, -1
        for other in range(self.length):
            if other not in ignore:
                if  self.adjacency_matrix[vertex][other] > max_weight:
                    max_weight = self.adjacency_matrix[vertex][other]
                    max_weight_edge_vertex = other
        return max_weight_edge_vertex

    def cut_component(self, cut_vertices):
        for row in xrange(self.length):
            for col in xrange(self.length):
                if row in cut_vertices or col in cut_vertices:
                    self.adjacency_matrix[row][col] = 0