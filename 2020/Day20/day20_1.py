file = open('input.txt', 'r')

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


def borders(tiles, n):
    tile = tiles[n]
    upper, lower = tile[0], tile[-1]
    left, right = '', ''
    for i in range(len(tile)):
        left += tile[i][0]
        right += tile[i][-1]
    return upper, lower, left, right, upper[::-1], lower[::-1], left[::-1], right[::-1]


def matches(tiles):
    match = {}
    for n in tiles:
        count, adj = 0, []
        for p in tiles:
            if n != p:
                bord = borders(tiles, p)
                for b in borders(tiles, n):
                    if b in bord:
                        adj += [p]
                        count += 1
                        break
        match[n] = (count, adj)
    return match


m = matches(tiles)
prod = 1
for i in tiles:
    if m[i][0] == 2:
        prod *= i

print(prod)
