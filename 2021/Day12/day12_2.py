file = open('input.txt', 'r')


def cave_connections(file):
    caves = {}
    for line in file:
        c = line[:-1].split('-')
        if c[0] not in caves:
            caves[c[0]] = [c[1]]
        else:
            caves[c[0]].append(c[1])
        if c[1] not in caves:
            caves[c[1]] = [c[0]]
        else:
            caves[c[1]].append(c[0])
    return caves


def create_adjacency(caves):
    all_caves = list(caves.keys())
    all_caves.remove('start')
    all_caves.remove('end')
    all_caves = ['start'] + all_caves + ['end']
    adj_mat = []
    for cave in all_caves:
        adj_mat.append([1 if i in caves[cave] else 0 for i in all_caves])
    return adj_mat, all_caves


def clear_col(m, indexes):
    a = [l[:] for l in m]
    for i in range(len(a)):
        for index in indexes:
            a[i][index] = 0
    return a


def count_paths(ad_mat, names, current_cave, clear_next, twice_visited):
    n_paths = 0
    o = names.index(current_cave)
    for cave in names:
        d = names.index(cave)
        if ad_mat[o][d] == 1:
            if d == len(ad_mat)-1:
                n_paths += 1
            else:
                if current_cave.islower():
                    if not twice_visited and current_cave != 'start':
                        if current_cave in clear_next:
                            if names[d] not in clear_next:
                                inds = [names.index(c) for c in clear_next]
                                n_paths += count_paths(clear_col(ad_mat, inds), names, names[d], clear_next, True)
                        else:
                            n_paths += count_paths(ad_mat, names, names[d], clear_next + [current_cave], twice_visited)
                    else:
                        n_paths += count_paths(clear_col(ad_mat, [o]), names, names[d], clear_next, twice_visited)
                else:
                    n_paths += count_paths(ad_mat, names, names[d], clear_next, twice_visited)
    return n_paths


caves = cave_connections(file)
adjacency_matrix, cave_names = create_adjacency(caves)
n = count_paths(adjacency_matrix, cave_names, 'start', [], False)
print(f'FINAL ANSWER: {n}')
