file = open('input.txt', 'r')

init = [int(n) for n in file.readline().split(',')]
start_dict = {}
for k in init:
    if k in start_dict:
        start_dict[k] += 1
    else:
        start_dict[k] = 1


def laternfish_simulation(occurrences, n_steps):
    for _ in range(n_steps):
        new_occ = {}
        for k in occurrences:
            if k == 0:
                new_occ[8] = occurrences[k]
                if 6 in new_occ:
                    new_occ[6] += occurrences[k]
                else:
                    new_occ[6] = occurrences[k]
            else:
                if k-1 == 6 and 6 in new_occ:
                    new_occ[k-1] += occurrences[k]
                else:
                    new_occ[k-1] = occurrences[k]
        occurrences = new_occ
    return occurrences


counts = laternfish_simulation(start_dict, 256)
print(f'FINAL ANSWER: {sum(counts.values())}')


