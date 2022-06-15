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
    polymer = start_poly
    for _ in range(n_steps):
        size = len(polymer)
        new_poly = ''
        for i in range(size-1):
            new_poly = new_poly + polymer[i]
            pair = polymer[i] + polymer[i+1]
            if pair in rules:
                new_poly = new_poly + rules[pair]
        new_poly = new_poly + polymer[i+1]
        polymer = new_poly
    return polymer


poly, rules = file_reader(file)
final_poly = polymerization(poly, rules, 10)
chars = set(final_poly)
occurrences = []
for char in chars:
    occurrences.append(final_poly.count(char))

print(f'FINAL ANSWER: {max(occurrences) - min(occurrences)}')