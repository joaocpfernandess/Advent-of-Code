file = open('input.txt', 'r')

instructions = []
visited = []
value = []
for line in file:
    line = line.split()
    instructions += [line[0]]
    sign, number = line[1][0], line[1][1:]
    value += [int(number) if sign == '+' else -1*int(number)]

accumulator = 0
current = 0  # Starting index
while current not in visited:
    visited += [current]
    to_do = instructions[current]
    if to_do == 'acc':
        accumulator += value[current]
        current += 1
    elif to_do == 'jmp':
        current += value[current]
    else:
        current += 1

print(accumulator)