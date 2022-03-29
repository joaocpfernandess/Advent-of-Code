import itertools
import numpy as np

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
            if r in [8, 11]:
                pass
            elif contains_only(base + order, rules[r]):
                order += [r]
                unvisited.remove(r)
                break
        if r == unvisited[-1]:
            break
    return base, order


def rule_constructor(base, order, rules):
    new_rules = {b: [rules[b]] for b in base}
    for l in order:
        possible = []
        for sublist in rules[l]:
            strings = [new_rules[r] for r in sublist]
            possible += [''.join(i) for i in itertools.product(*strings)]
        new_rules[l] = list(set(possible))
    return new_rules

base, order = rule_order(rules)
base_valid = rule_constructor(base, order + [8, 11, 0], rules)[0]

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

base, order = rule_order(rules)
new_rules = rule_constructor(base, order, rules)

rule42 = new_rules[42]
rule31 = new_rules[31]
# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

# Possibly valid messages: 42 42 31 (BASE) | 42 42 31 31 | 42 (...) 42 31
# If a message matches base_valid: great
# Else:
#    Case #1: Add rule-42 messages until len is surpassed
#    Case #2: Add simultaneously rule-42 in the beginning and rule-31 in the end
# NOTE: BOTH RULES ONLY HAVE 8-LEN STRINGS


def add42(message, rule42):
    while len(message) != 0:
        sub = message[-8:]
        if sub in rule42:
            message = message[:-8]
        else:
            return False
    return True


def add31(message, rule42, rule31):
    n = len(message[1])
    while len(message[1]) != 0:
        sub = message[1][:8]
        if sub in rule31:
            message[1] = message[1][8:]
        else:
            return False
    return add42(message[0], rule42) and n <= len(message[0])


i = 0
count = 0
for message in messages:
    if message in base_valid:
        print(f'Message {i+1}: valid')
        count += 1
    else:
        stop = False
        subs = [i for i in base_valid if len(i) < len(message)]
        for s in subs:
            if s in message:
                indexes = [index for index in range(len(message)) if message.startswith(s, index)]
                for j in indexes:
                    nmessage = [message[:j], message[j+len(s):]]
                    if add31(nmessage, rule42, rule31):
                        print(f'Message {i + 1}: valid')
                        count += 1
                        stop = True
            if stop:
                break
        if not stop:
            print(f'Message {i + 1}: invalid')
    i += 1

print(count)
