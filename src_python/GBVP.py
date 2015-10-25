__author__ = 'kushasharma'
from GBVP_graph import GBVP_graph
from linear_tree import linear_tree
from affinity_cycle import affinity_cycle

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

if __name__ == '__main__':
    gbvp_graph = GBVP_graph(ADJ_MAT)
    tree = linear_tree(8, gbvp_graph)
    while not tree.primitive_cycle:
        if not tree.extend():
            print "no more edges to extend!"
            break
    if tree.primitive_cycle:
        print "primitive cycle found"
        print tree.vertices
        an_affinity_cylce = affinity_cycle(tree.vertices, gbvp_graph, tree.primitive_cycle_at_higher)
        print an_affinity_cylce



