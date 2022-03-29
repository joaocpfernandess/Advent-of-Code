file = open('input.txt', 'r')


# Auxiliary function to determine the validity of a ticket
def validQ(intervals, n):
    for t in intervals:
        if (t[0] < n < t[1]) or (t[2] < n < t[3]):
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


invalid += [n]
for ticket in nearbytickets:
    for n in ticket:
        if not validQ(list(ranges.values()), n):
            invalid += [n]


print(sum(invalid))