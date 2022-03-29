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


def adjacent_pos(board, i, j, max_i, max_j):

    def expand(pos):
        where = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]
        for i in range(8):
            if pos[i]:
                pos[i] = [pos[i][0] + where[i][0], pos[i][1] + where[i][1]]

    locked = 0
    res = []
    start = [[i,j] for _ in range(8)]
    while locked != 8:
        expand(start)
        for p in range(8):
            if start[p]:
                if start[p][0] < 0 or start[p][0] > max_i or start[p][1] < 0 or start[p][1] > max_j:
                    locked += 1
                    start[p] = None
                elif board[start[p][0]][start[p][1]] == '#':
                    locked += 1
                    res += [start[p]]
                    start[p] = None
                elif board[start[p][0]][start[p][1]] == 'L':
                    locked += 1
                    res += [start[p]]
                    start[p] = None
    return res


changes = None
while changes != 0:
    changes = 0
    new = []
    for i in range(maxi + 1):
        add = []
        for j in range(maxj + 1):
            if current[i][j] == '#':
                if len([pos for pos in adjacent_pos(current,i,j,maxi,maxj) if current[pos[0]][pos[1]]=='#']) >= 5:
                    add += [change_seat(current, i, j)]
                    changes += 1
                else:
                    add += [current[i][j]]
            elif current[i][j] == 'L':
                if all(list(map(lambda x: True if current[x[0]][x[1]] != '#' else False, adjacent_pos(current, i, j, maxi, maxj)))):
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
