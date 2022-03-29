import itertools

file = open('input.txt', 'r')

rules = {}
messages = []
part = 1
for line in file:
    if line == '\n':
        part = 2
        line = file.readline()
    if part == 1:
        line = line[:-1].split(': ')
        line[1] = line[1].split(' | ')
        try:
            rules[int(line[0])] = [[int(i) for i in s.split(' ')] for s in line[1]]
        except ValueError:
            rules[int(line[0])] = line[1][0][1]
    else:
        messages += [line[:-1]]


def contains_only(nodes, rule):
    flat = [s for i in rule for s in i]
    return all([True if f in nodes else False for f in flat])


def rule_order(rules):
    unvisited = list(rules.keys())
    base = []
    for i in rules:
        if type(rules[i]) == str:
            base += [i]
            unvisited.remove(i)
    order = []
    while len(unvisited) != 0:
        for r in unvisited:
            if contains_only(base + order, rules[r]):
                order += [r]
                unvisited.remove(r)
                break
    return base, order


def rule_constructor(base, order, rules):
    new_rules = {b: [rules[b]] for b in base}
    for l in order:
        possible = []
        for sublist in rules[l]:
            strings = [new_rules[r] for r in sublist]
            possible += [''.join(i) for i in itertools.product(*strings)]
        new_rules[l] = possible
    return new_rules


base, order = rule_order(rules)
print(order)
valid_messages = rule_constructor(base, order, rules)[0]

count = 0
for message in messages:
    if message in valid_messages:
        count += 1

print(count)


