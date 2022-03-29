import numpy as np
print(np.cos(np.deg2rad(90)))
file = open('input.txt', 'r')

instructions, values = [], []
for line in file:
    instructions += [line[0]]
    values += [int(line[1:len(line)-1])]

# Starting position is taken as (0,0)
# West and south are taken as the negative values of the x and y axis respectively
pos = [0, 0]
waypoint = [10, 1]

for i in range(len(instructions)):
    if instructions[i] in ['W', 'E']:
        d = 1 if instructions[i] == 'E' else -1
        waypoint[0] += values[i] * d
    elif instructions[i] in ['N', 'S']:
        d = 1 if instructions[i] == 'N' else -1
        waypoint[1] += values[i] * d
    elif instructions[i] in ['L', 'R']:
        turns = 360 - values[i] if instructions[i] == 'R' else values[i]
        waypoint = np.matmul([[np.cos(np.deg2rad(turns)), -np.sin(np.deg2rad(turns))], [np.sin(np.deg2rad(turns)), np.cos(np.deg2rad(turns))]], waypoint)
    elif instructions[i] == 'F':
        pos = [pos[j] + waypoint[j]*values[i] for j in range(2)]

print(pos)
print(sum([abs(p) for p in pos]))