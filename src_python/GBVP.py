__author__ = 'kushasharma'
from collections import deque


SAMPLE_MAT = [[ 0,  25,  25,   0,  75,   0,  50,  25,  25,   0],
              [ 25,   0,  75,   0,  25,   0,  60, 110,  75,   0],
              [ 25,  75,   0,  15,  25,  15,  25,  75, 115,  15],
              [ 0,    0,  15,   0,   0,  40,   0,   0,  15,  40],
              [ 75,  25,  25,   0,   0,   0,  50,  25,  25,   0],
              [ 0,    0,  15,  40,   0,   0,   0,   0,  15,  40],
              [ 50,  60,  25,   0,  50,   0,   0,  60,  25,   0],
              [ 25, 110,  75,   0,  25,   0,  60,   0,  75,   0],
              [ 25,  75, 115,  15,  25,  15,  25,  75,   0,  15],
              [  0,   0,  15,  40,   0,  40,   0,   0,  15,   0]]

ADJ_MAT = SAMPLE_MAT
LENGTH = len(ADJ_MAT)

def get_max_weight_edge_vertex(vertex, ignore_vertex = None):
    max_weight, max_weight_edge_vertex = 0, 0
    for other in range(LENGTH):
        if not other == ignore_vertex and not other == vertex:
            if  ADJ_MAT[vertex][other] > max_weight:
                max_weight = ADJ_MAT[vertex][other]
                max_weight_edge_vertex = other
    return max_weight_edge_vertex

class linear_tree:
    def __init__(self, start_vertex):
        self.edges = set()
        max_weight_eddge_vertex = get_max_weight_edge_vertex(start_vertex)
        self.vertices = deque([start_vertex, max_weight_eddge_vertex])
        self.lower_end = start_vertex
        self.higher_end = max_weight_eddge_vertex
        self.primitive_cycle = False

    def max_edge_at_lower_end(self):
        return get_max_weight_edge_vertex(self.lower_end, self.vertices[1])

    def max_edge_at_higher_end(self):
        return get_max_weight_edge_vertex(self.higher_end, self.vertices[len(self.vertices) - 2])

    def check_for_primitive_cycle(self, vertex, higher = True):
        if higher:
            for idx in xrange(len(self.vertices) - 1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True
        else:
            for idx in xrange(len(self.vertices) - 1, 0, -1):
                if self.vertices[idx] == vertex:
                    self.primitive_cycle = True

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

if __name__ == '__main__':
    tree = linear_tree(8)
    while not tree.primitive_cycle:
        if not tree.extend():
            print "no more edges to extend!"
            break
    if tree.primitive_cycle:
        print "primitive cycle found"
        print tree.vertices





