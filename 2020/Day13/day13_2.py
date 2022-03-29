import functools as f

file = open('input.txt', 'r')
file.readline()

line = file.readline().split(',')

ids_offset = []   # [[17, 0], [41, 7], [523, 17], [13, 35], [19, 36], [23, 40], [787, 48], [37, 54], [29, 77]]
for i in line:
    try:
        ids_offset += [[int(i), line.index(i)]]
    except ValueError:
        pass


def coprimeQ(w):
    for i in range(len(w)-1):
        for j in range(i+1, len(w)):
            if w[i] % w[j] == 0 or w[j] % w[i] == 0:
                return False
    return True


def chinese_remainder_theorem(a, mods):

    def solver(a, b, m):
        k = 0
        while a*k % m != b and k < m:
            k += 1
        return k

    c = a[0] % mods[0]
    for i in range(1, len(a)):
        m = f.reduce(lambda a, b: a*b, [mods[k] for k in range(i)])
        z = solver(m, (a[i]-c) % mods[i], mods[i])
        c += z * m
    return c


print(chinese_remainder_theorem([i[0]-i[1] for i in ids_offset], [i[0] for i in ids_offset]))

