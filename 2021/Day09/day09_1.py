file = open('input.txt', 'r')


def gridify(file):
    grid = []
    for line in file:
        add = []
        for l in line[:-1]:
            add.append(int(l))
        grid.append(add)
    return grid


def neighbours(grid, pos):
    x, y = pos[0], pos[1]
    xmax, ymax = len(grid)-1, len(grid[0])-1
    neigh = []
    neigh = neigh + [grid[x][y+1]] if y != ymax else neigh
    neigh = neigh + [grid[x][y-1]] if y != 0 else neigh
    neigh = neigh + [grid[x+1][y]] if x != xmax else neigh
    neigh = neigh + [grid[x-1][y]] if x != 0 else neigh
    return neigh


g = gridify(file)
n, m = len(g), len(g[0])
res = 0
for i in range(n):
    for j in range(m):
        pos = [i, j]
        neighbs = neighbours(g, pos)
        if all(map(lambda x: x > g[i][j], neighbs)):
            res += 1 + g[i][j]
            

print(f'FINAL RESULT: {res}')