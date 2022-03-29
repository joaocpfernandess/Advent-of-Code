file = open('input.txt', 'r')

current = []
for line in file:
    add = []
    for letter in line:
        add += [letter]
    current += [add]
maxi = len(current) - 1
maxj = len(current[0]) - 1


def change_seat(seats, i, j):
    return 'L' if seats[i][j] == '#' else '#'


def adjacent_pos(i, j, max_i, max_j):
    res = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    if i == 0:
        res.remove([i-1, j-1])
        res.remove([i-1, j])
        res.remove([i-1, j+1])
    elif i == max_i:
        res.remove([i+1, j-1])
        res.remove([i+1, j])
        res.remove([i+1, j+1])
    if j == 0:
        if i != 0:
            res.remove([i-1, j-1])
        res.remove([i, j-1])
        if i != max_i:
            res.remove([i+1, j-1])
    elif j == max_j:
        if i != 0:
            res.remove([i-1, j+1])
        res.remove([i, j+1])
        if i != max_i:
            res.remove([i+1, j+1])
    return res


changes = None
while changes != 0:
    changes = 0
    new = []
    for i in range(maxi + 1):
        add = []
        for j in range(maxj + 1):
            if current[i][j] == '#':
                if len([pos for pos in adjacent_pos(i,j,maxi,maxj) if current[pos[0]][pos[1]]=='#']) >= 4:
                    add += [change_seat(current, i, j)]
                    changes += 1
                else:
                    add += [current[i][j]]
            elif current[i][j] == 'L':
                if all(list(map(lambda x: True if current[x[0]][x[1]] != '#' else False, adjacent_pos(i, j, maxi, maxj)))):
                    add += [change_seat(current, i, j)]
                    changes += 1
                else:
                    add += [current[i][j]]
            else:
                add += [current[i][j]]
        new += [add]
    current = new

occupied = 0
for i in range(maxi+1):
    for j in range(maxj+1):
        if current[i][j] == '#':
            occupied += 1

print("FINAL ANSWER: {}".format(occupied))







