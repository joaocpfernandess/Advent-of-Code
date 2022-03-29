file = open('input.txt', 'r')

instructions, values = [], []
for line in file:
    instructions += [line[0]]
    values += [int(line[1:len(line)-1])]

# Starting position is taken as (0,0)
# West and south are taken as the negative values of the x and y axis respectively

pos = [0, 0]
facing = [1, 0]
faces = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(len(instructions)):
    if instructions[i] in ['W', 'E']:
        d = 1 if instructions[i] == 'E' else -1
        pos[0] += values[i] * d
    elif instructions[i] in ['N', 'S']:
        d = 1 if instructions[i] == 'N' else -1
        pos[1] += values[i] * d
    elif instructions[i] in ['L', 'R']:
        turns = int((360 - values[i])/90) if instructions[i] == 'R' else int(values[i]/90)
        facing = faces[(faces.index(facing)+turns) % 4]
    elif instructions[i] == 'F':
        pos = [pos[j] + facing[j]*values[i] for j in range(2)]

print(pos)
print(sum([abs(p) for p in pos]))







