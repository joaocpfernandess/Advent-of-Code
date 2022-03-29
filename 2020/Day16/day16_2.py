file = open('input.txt', 'r')


# Auxiliary function to determine the validity of a ticket
def validQ(intervals, n):
    for t in intervals:
        if (t[0] <= n <= t[1]) or (t[2] <= n <= t[3]):
            return True
    return False


def validQ2(t, n):
    if (t[0] <= n <= t[1]) or (t[2] <= n <= t[3]):
        return True
    return False


# Input reader
ranges = {}
for line in file:
    if line == 'your ticket:\n':
        myticket = file.readline()[:-1]
        myticket = [int(i) for i in myticket.split(',')]
    elif line == 'nearby tickets:\n':
        nearbytickets = []
        for line in file:
            nearbytickets += [[int(i) for i in line.split(',')]]
    elif line != '\n':
        line = line.split(': ')
        intervals = line[1].replace('\n','').split(' or ',)
        ranges[line[0]] = [int(i) for r in intervals for i in r.split('-')]


# Determining the valid tickets
validtickets = []
for ticket in nearbytickets:
    if all([validQ(list(ranges.values()), n) for n in ticket]):
        validtickets += [ticket]


# Determining the attribute of each column
attributes = list(ranges.keys())
ordered = [None for _ in range(len(attributes))]
bycol = [[validtickets[i][j] for i in range(len(validtickets))] for j in range(len(validtickets[0]))]

cloned_cols = bycol.copy()
while attributes:
    could_be = {}
    for att in attributes:
        for col in bycol:
            if all([validQ2(ranges[att], n) for n in col]):
                if att not in could_be:
                    could_be[att] = [col]
                else:
                    could_be[att] += [col]
    for att_key in could_be:
        if len(could_be[att_key]) == 1:
            ordered[cloned_cols.index(could_be[att_key][0])] = att_key
            attributes.remove(att_key)
            bycol.remove(could_be[att_key][0])
            break


prod = 1
for i in range(len(ordered)):
    if ordered[i].startswith('departure'):
        prod *= myticket[i]

print(prod)








