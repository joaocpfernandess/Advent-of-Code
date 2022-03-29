file = open('input.txt', 'r')


start = []
y = 0
for line in file:
    line = line[:-1]
    for x in range(len(line)):
        if line[x] == '#':
            start += [[x, y, 0, 0]]
    y += 1


def neighbours(coord):
    return [[coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+p] for i in [-1, 0, 1] for j in [-1, 0, 1] for k in [-1, 0, 1] for p in [-1, 0, 1]]


def active_neighbours(all_actives, coord):
    n = 0
    neigh = neighbours(coord)
    for act in all_actives:
        if act in neigh and act != coord:
            n += 1
    return n


def inactive_candidates(all_actives):
    possible = []
    for c in all_actives:
        for neigh in neighbours(c):
            if neigh not in all_actives and neigh not in possible:
                possible += [neigh]
    return possible


def cycle_simulator(start, cycles):
    active = start
    for q in range(cycles):
        new = []
        for c in active:
            if active_neighbours(active, c) in [2, 3]:
                new += [c]
        for i in inactive_candidates(active):
            if active_neighbours(active, i) == 3:
                new += [i]
        active = new.copy()
        print(f'End of cycle {q+1}: {len(active)} active cubes')
    return len(active)


print(cycle_simulator(start, 6))