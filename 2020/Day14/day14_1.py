file = open('input.txt', 'r')

def bit_to_int(b):
    return sum([2**(35-i)*int(b[i]) for i in range(36)])


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
        if mask[i] != 'X':
            bit[i] = mask[i]
    return bit


memory = {}
mask = ['X' for _ in range(36)]
for line in file:
    line = line.split(' = ')
    if line[0] == 'mask':
        mask = [p for p in line[1][:-1]]
    else:
        num_bit = int_to_bit(int(line[1][:-1]))
        num = bit_to_int(masking(mask, num_bit))
        memory[int(line[0][4:-1])] = num

print(memory)
print(sum(list(memory.values())))