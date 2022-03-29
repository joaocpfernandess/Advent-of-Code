file = open('input.txt', 'r')


def priority_tracker(line):
    priority = []
    par = 0
    for i in range(len(line)):
        if line[i] == '(':
            par += 1
            priority += ['(']
        elif line[i] == ')':
            par -= 1
            priority += [')']
        elif line[i] in ['+', '*']:
            priority += [line[i]]
        else:
            priority += [par]
    return priority


def part_calculate(sequence):   # Input should be a sequence of same-priority operations
    while len(sequence) != 1:
        for i in range(len(sequence)):
            if sequence[i] == '+':
                sequence = sequence[:i-1] + [sequence[i-1]+sequence[i+1]] + sequence[i+2:]
                break
            elif sequence[i] == '*':
                if '+' not in sequence:
                    sequence = sequence[:i-1] + [sequence[i-1]*sequence[i+1]] + sequence[i+2:]
                    break
    return sequence[0]


def calculate(line):
    prio = priority_tracker(line)
    while not all(map(lambda x: True if x == 0 else False, [i for i in prio if type(i) == int])):
        max_prio = max([i for i in prio if type(i) == int])
        s = prio.index(max_prio)
        sequence = []
        e = s
        while line[e] != ')':
            sequence += [line[e]]
            e += 1
        res = part_calculate(sequence)
        line = line[:s-1] + [res] + line[e+1:]
        prio = prio[:s-1] + [max_prio-1] + prio[e+1:]
    return part_calculate(line)


results = []
for line in file:
    line = [i for c in line[:-1].split(' ') for i in c]
    line = [int(i) if i.isnumeric() else i for i in line]
    results += [calculate(line)]

print(sum(results))
