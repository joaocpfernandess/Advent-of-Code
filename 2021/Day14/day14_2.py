file = open('input.txt', 'r')


def file_reader(f):
    polymer = f.readline()[:-1]
    f.readline()
    rules = {}
    for line in f:
        line = line[:-1].split(' -> ')
        rules[line[0]] = line[1]
    return polymer, rules


def polymerization(start_poly, rules, n_steps):
    size = len(start_poly)
    pairs_count = {}
    for i in range(size-1):
        pair = start_poly[i] + start_poly[i+1]
        if pair not in pairs_count:
            pairs_count[pair] = 1
        else:
            pairs_count[pair] += 1
    for j in range(n_steps):
        #print(f'STEP {j+1}')
        new_pairs = {}
        for pair in pairs_count:
            if pair in rules:
                if pair[0] + rules[pair] not in new_pairs:
                    new_pairs[pair[0] + rules[pair]] = pairs_count[pair]
                else:
                    new_pairs[pair[0] + rules[pair]] += pairs_count[pair]
                if rules[pair] + pair[1] not in new_pairs:
                    new_pairs[rules[pair] + pair[1]] = pairs_count[pair]
                else:
                    new_pairs[rules[pair] + pair[1]] += pairs_count[pair]
            else:
                if pair not in new_pairs:
                    new_pairs[pair] = pairs_count[pair]
                else:
                    new_pairs[pair] += pairs_count[pair]
        pairs_count = new_pairs
    return pairs_count


def counting_occurrences(pair_count, first_char, last_char):
    occurrences = {first_char: 1, last_char: 1}
    for pair in pair_count:
        for char in pair:
            if char not in occurrences:
                occurrences[char] = pair_count[pair]
            else:
                occurrences[char] += pair_count[pair]
    for c in occurrences:
        occurrences[c] = int(occurrences[c]/2)
    return occurrences


poly, rules = file_reader(file)
first_char, last_char = poly[0], poly[-1]
pairs = polymerization(poly, rules, 40)
occ = counting_occurrences(pairs, first_char, last_char)


print(f'FINAL ANSWER: {max(occ.values()) - min(occ.values())}')