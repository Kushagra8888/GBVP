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

class edge:
    def __init__(self, v1, v2):
        if v1 > v2:
            self.vertices = (v2, v1)
        else:
            self.vertices = (v1, v2)

    def weight(self, ADJ_MAT):
        return ADJ_MAT[self.vertices[0]][self.vertices[1]]

    def __str__(self):
        return "(" + str(self.vertices[0]) + "," + str(self.vertices[1]) + ")"

    def __repr__(self):
        return "(" + str(self.vertices[0]) + "," + str(self.vertices[1]) + ")"


class affinity_cycle:
    def __init__(self, vertex_list, higher = True):
        self.edges = set([])
        if higher:
            self.cycle_node = vertex_list[-1]
            self.other_node = vertex_list[-2]
            start_idx = len(vertex_list) - 1
            idx = start_idx
            while(idx == start_idx or vertex_list[idx] != self.cycle_node):
                self.edges.add(edge(vertex_list[idx], vertex_list[idx - 1]))
                idx -= 1
        else:
            self.cycle_node = vertex_list[0]
            self.other_node = vertex_list[1]
            start_idx = 0
            idx = start_idx
            while(idx == start_idx or vertex_list[idx] != self.cycle_node):
                self.edges.add(edge(vertex_list[idx], vertex_list[idx + 1]))
                idx += 1

    def __str__(self):
        return "\nAffinity Cycle: " + "\nCycle Node: " + str(self.cycle_node) + "\nOther Node: " + str(self.other_node)\
               + "\nEdges: " + str(self.edges)


class linear_tree:
    def __init__(self, start_vertex):
        self.edges = set()
        max_weight_eddge_vertex = get_max_weight_edge_vertex(start_vertex)
        self.vertices = deque([start_vertex, max_weight_eddge_vertex])
        self.lower_end = start_vertex
        self.higher_end = max_weight_eddge_vertex
        self.primitive_cycle = False
        self.primitive_cycle_at_higher = True

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

if __name__ == '__main__':
    tree = linear_tree(8)
    while not tree.primitive_cycle:
        if not tree.extend():
            print "no more edges to extend!"
            break
    if tree.primitive_cycle:
        print "primitive cycle found"
        print tree.vertices
        an_affinity_cylce = affinity_cycle(tree.vertices, tree.primitive_cycle_at_higher)
        print an_affinity_cylce



