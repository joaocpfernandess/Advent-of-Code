file = open('input.txt', 'r')


def gridify(file):
    grid = []
    for line in file:
        add = []
        for l in line[:-1]:
            if l != '9':
                add.append(int(l))
            else:
                add.append('X')
        grid.append(add)
    return grid


def non_null_neighbours(grid, pos):
    x, y = pos[0], pos[1]
    grid[x][y] = 'X'
    xmax, ymax = len(grid)-1, len(grid[0])-1
    neigh = []
    neigh = neigh + [[x, y+1]] if y != ymax and grid[x][y+1] != 'X' else neigh
    neigh = neigh + [[x, y-1]] if y != 0 and grid[x][y-1] != 'X' else neigh
    neigh = neigh + [[x+1, y]] if x != xmax and grid[x+1][y] != 'X' else neigh
    neigh = neigh + [[x-1, y]] if x != 0 and grid[x-1][y] != 'X' else neigh
    return neigh


g = gridify(file)
basins = []
n, m = len(g), len(g[0])
for i in range(n):
    for j in range(m):
        if g[i][j] != 'X':
            queue = [[i, j]]
            s = 1
            while queue:
                next_queue = non_null_neighbours(g, queue[0])
                queue = queue[1:]
                next_queue = [i for i in next_queue if i not in queue]
                s += len(next_queue)
                queue = queue + next_queue
            basins.append(s)


basins.sort()
print(f'FINAL ANSWER: {basins[-1] * basins[-2] * basins[-3]}')

