file = open('input.txt', 'r')


def gridify(file):
    grid = []
    for line in file:
        add = []
        for c in line[:-1]:
            add.append(int(c))
        grid.append(add)
    return grid


def neighbours(coord, maxx, maxy):
    temp = [[coord[0]+i, coord[1]+j] for i in [-1, 0, 1] for j in [-1, 0, 1]]
    res = []
    for pair in temp:
        if 0 <= pair[0] <= maxx and 0 <= pair[1] <= maxy and pair != coord:
            res.append(pair)
    return res


def reset_grid(grid, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 9:
                grid[i][j] = 0
    return grid


def add_one(grid, n, m):
    flashing = []
    for i in range(n):
        for j in range(m):
            grid[i][j] += 1
            if grid[i][j] > 9:
                flashing.append([i, j])
    return grid, flashing


def add_to_neighbours(queue, grid, maxx, maxy):
    flashed = queue
    while queue:
        curr = queue[0]
        queue = queue[1:]
        neighs = neighbours(curr, maxx, maxy)
        for nei in neighs:
            grid[nei[0]][nei[1]] += 1
            if grid[nei[0]][nei[1]] > 9 and nei not in flashed:
                queue.append(nei)
                flashed.append(nei)
    return grid, len(flashed)


g = gridify(file)
n, m = len(g), len(g[0])
maxx, maxy = n-1, m-1
n_flash = 0
step = 0
while n_flash != n*m:
    g, flashing = add_one(g, n, m)
    g, n_flash = add_to_neighbours(flashing, g, maxx, maxy)
    g = reset_grid(g, n, m)
    step += 1


print(f'FINAL ANSWER: {step}')
