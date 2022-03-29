file = open('input.txt', 'r')


def bit_to_int(b):
    fixed, variable = 0, []
    for i in range(36):
        if b[i] != 'X':
            fixed += 2**(35-i)*int(b[i])
        else:
            f1, f2 = lambda x: x, lambda x: x + 2**(35-i)
            variable = [f(v) for v in variable for f in (f1, f2)]
    return [fixed] if variable == [] else [fixed + v for v in variable]


def int_to_bit(n):
    bitlist = []
    for j in range(36):
        if n >= (2**(35-j)):
            bitlist += [1]
            n -= 2**(35-j)
        else:
            bitlist += [0]
    return bitlist


def masking(mask, bit):
    for i in range(36):
        if mask[i] != '0':
            bit[i] = mask[i]
    return bit


memory = {}
mask = ['X' for _ in range(36)]
for line in file:
    line = line.split(' = ')
    if line[0] == 'mask':
        mask = [p for p in line[1][:-1]]
    else:
        num_bit = int_to_bit(int(line[0][4:-1]))
        mems = bit_to_int(masking(mask, num_bit))
        for m in mems:
            memory[m] = int(line[1][:-1])

#print(memory)
print(sum(memory.values()))