import numpy as np

class Grid:

    def __init__(self, dim):
        self.dim = dim
        self.height = dim[0]
        self.width = dim[1]
        self.marks = np.zeros((self.height, self.width))

    def markupline(self, pts):  # pts -> [[x1,y1],[x2,y2]]
        if pts[0][0] == pts[1][0]:
            p = min(pts[0][1], pts[1][1])
            while p != max(pts[0][1], pts[1][1]):
                self.marks[pts[0][0]][p] += 1
                p += 1
            self.marks[pts[0][0]][p] += 1
        elif pts[0][1] == pts[1][1]:
            p = min(pts[0][0], pts[1][0])
            while p != max(pts[0][0], pts[1][0]):
                self.marks[p][pts[0][1]] += 1
                p += 1
            self.marks[p][pts[0][1]] += 1
        else:
            ref = 0 if pts[0][0] < pts[1][0] else 1
            p, q = pts[ref][0], pts[ref][1]
            d = 1 if pts[ref][1] < pts[1-ref][1] else -1
            while p != max(pts[0][0], pts[1][0]):
                self.marks[p][q] += 1
                p += 1
                q += d
            self.marks[p][q] += 1

    def dangercells(self):
        res = []
        for i in range(self.height):
            for j in range(self.width):
                if self.marks[i][j] >= 2:
                    res += [[i,j]]
        return res


def line_reader(line):
    line = line.split()
    pt1 = [int(n) for n in line[0].split(',')]
    pt2 = [int(n) for n in line[2].split(',')]
    return [pt1, pt2]


file = open('input.txt', 'r')
lines = []
h, w = 0, 0
for line in file:
    m = line_reader(line)
    lines += [m]
    if m[0][0] > h or m[1][0] > h:
        h = max(m[0][0], m[1][0])
    if m[0][1] > w or m[1][1] > w:
        w = max(m[0][1], m[1][1])

check = []
g = Grid((h+1,w+1))
for l in lines:
    g.markupline(l)
print(len(g.dangercells()))