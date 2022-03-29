file = open('input.txt', 'r')


def borders(tiles, n):
    tile = tiles[n]
    upper, lower = tile[0], tile[-1]
    left, right = '', ''
    for i in range(len(tile)):
        left += tile[i][0]
        right += tile[i][-1]
    return upper, left, lower, right, upper[::-1], left[::-1], lower[::-1], right[::-1]


def matches(tiles, border):
    match = {}
    for n in tiles:
        count, adj, orientation = 0, [], []
        for p in tiles:
            if p != n:
                bord_p = border[p]
                bord_n = border[n]
                for b in range(len(bord_p)):
                    if bord_p[b] in bord_n:
                        adj += [p]
                        orientation += [(bord_n.index(bord_p[b])%4) + 1]
                        count += 1
                        break
        match[n] = (count, adj, orientation)
    return match


def remove_border(tile):
    return [tile[i][1:-1] for i in range(1, len(tile)-1)]


def construct_outer(corners, edges):
    unvisited = [i for i in corners] + [j for j in edges]
    lines = []
    for k in range(4):
        start_corner = unvisited[k]
        unvisited.remove(start_corner)
        next = corners[start_corner][1][0] if corners[start_corner][1][0] in unvisited else corners[start_corner][1][1]
        addline = [start_corner, next]
        while next not in corners:
            for p in range(3):
                if edges[next][1][p] in unvisited:
                    unvisited.remove(next)
                    next = edges[next][1][p]
                    addline += [next]
                    break
        lines += [addline]
        unvisited = [start_corner] + unvisited
    return lines


def puzzle_grid(outer, middle):

    # Constructing the outer grid
    grid, n = [outer[0]], len(outer[0])
    for i in [1, 2, 3]:
        if outer[i][0] == outer[0][0]:
            left_line = outer[i]
        elif outer[i][-1] == outer[0][0]:
            outer[i].reverse()
            left_line = outer[i]
        elif outer[i][0] == outer[0][-1]:
            right_line = outer[i]
        elif outer[i][-1] == outer[0][-1]:
            outer[i].reverse()
            right_line = outer[i]
        else:
            bottom_line = outer[i]
    if bottom_line[0] != left_line[-1]:
        bottom_line.reverse()
    for j in range(1, n-1):
        grid += [[left_line[j]] + [None for _ in range(n-2)] + [right_line[j]]]
    grid += [bottom_line]

    # Joining the middle pieces
    unvisited = list(middle.keys())
    for p in range(1, n-1):
        for q in range(1, n-1):
            neighbours = set(filter(None, [grid[p][q-1], grid[p][q+1], grid[p-1][q], grid[p+1][q]]))
            piece = [key for key in middle if key in unvisited and neighbours.issubset(set(middle[key][1]))][0]
            grid[p][q] = piece
            unvisited.remove(piece)

    return grid


def rotating_pieces(grid, matches, tiles):
    n = len(grid)
    orientation = [] # Pair (B, n): -> B is boolean True if flip else False, n gives rotation (after flip if B)
    for i in range(n):
        add = []
        for j in range(n):
            elem = grid[i][j]
            steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            sides, diffs = [], []
            for pair in steps:
                if 0 <= i+pair[0] < n and 0 <= j+pair[1] < n:
                    e = grid[i+pair[0]][j+pair[1]]
                    sides += [[matches[elem][2][matches[elem][1].index(e)], steps.index(pair)+1]]
                    diffs += [sides[-1][1]-sides[-1][0] if sides[-1][1]-sides[-1][0] >= 0 else sides[-1][1]-sides[-1][0]+4]
            if not all(map(lambda x: True if x == diffs[0] else False, diffs[1:])):
                B = True
                for s in sides:
                    if s[0] == 2:
                        s[0] = 4
                    elif s[0] == 4:
                        s[0] = 2
            else:
                B = False
            n_rot = sides[0][1] - sides[0][0] if sides[0][1] - sides[0][0] >= 0 else sides[0][1]+4-sides[0][0]
            add += [(B, n_rot)]
        orientation += [add]
    return orientation


def rotate_flip_piece(tile, orientation):
    if orientation[0]:
        newtile = []
        for line in tile:
            line = list(line)
            line.reverse()
            newtile += [''.join(line)]
        tile = newtile
    for _ in range(orientation[1]):
        tile = list(reversed(list(zip(*tile))))
    return list(map(lambda x: list(x), tile))


def assemble_image(grid, tiles, orientation):
    n = len(grid)
    p = len(list(tiles.values())[0]) - 2
    image = []
    for i in range(n):
        row = [[] for _ in range(p)]
        for j in range(n):
            key = grid[i][j]
            tile = tiles[key]
            orient = orientation[i][j]
            piece = rotate_flip_piece(tile, orient)
            piece = remove_border(piece)
            for k in range(p):
                row[k] += piece[k]
        image += [''.join(r) for r in row]
    return image


def sea_monster_searcher(image, coords):
    n = len(image)
    sea_monsters = 0
    height, length = max([i[0] for i in coords]), max([i[1] for i in coords])
    for i in range(n-height):
        for j in range(n-length):
            p = 0
            while p < len(coords) and image[i+coords[p][0]][j+coords[p][1]] == '#':
                p += 1
            if p == len(coords):
                sea_monsters += 1
    return sea_monsters


tiles = {}
for line in file:
    if line[0] == 'T':
        number = int(line.split(' ')[1][:-2])
        tile = []
        line = file.readline()
        while line != '\n':
            tile += [line[:-1]]
            line = file.readline()
        tiles[number] = tile

border = {}
for n in tiles:
    border[n] = borders(tiles, n)

m = matches(tiles, border)

corner_matches, edge_matches, middle_matches = {}, {}, {}
for i in tiles:
    if m[i][0] == 2:
        corner_matches[i] = m[i]
    elif m[i][0] == 3:
        edge_matches[i] = m[i]
    else:
        middle_matches[i] = m[i]

out = construct_outer(corner_matches, edge_matches)
grid = puzzle_grid(out, middle_matches)
orientation = rotating_pieces(grid, m, tiles)
image = assemble_image(grid, tiles, orientation)

sea_monster_coord = [(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11),
                     (1, 12), (2, 13), (2, 16), (1, 17), (1, 18), (1, 19), (0, 18)]
n_asterisks = 0
for m in range(len(image)):
    for k in range(len(image)):
        if image[m][k] == '#':
            n_asterisks += 1
n_sea_monsters = sea_monster_searcher(image, sea_monster_coord)
result = n_asterisks - (n_sea_monsters * len(sea_monster_coord))

print(f'FINAL RESULT: {result}')









