__author__ = 'kushasharma'

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

    def __hash__(self):
        return self.vertices[0] ** 2 + self.vertices[1] ** 2

    def __eq__(self, other):
        return self.vertices == other.vertices