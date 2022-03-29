file = open('input.txt', 'r')
valid = 0
for line in file:
    a = line.split()
    limit = ['', '']
    i = 0
    for p in a[0]:
        if p != '-':
            limit[i] += p
        else:
            i += 1
    limit = [int(limit[0]), int(limit[1])]
    letter = a[1][0]
    n = 0
    for l in a[2]:
        if l == letter:
            n += 1
    if n >= limit[0] and n <= limit[1]:
        valid += 1

print(valid)



