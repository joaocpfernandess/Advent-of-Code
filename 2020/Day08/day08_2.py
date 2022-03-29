file = open('input.txt', 'r')

instructions = []
value = []
for line in file:
    line = line.split()
    instructions += [line[0]]
    sign, number = line[1][0], line[1][1:]
    value += [int(number) if sign == '+' else -1*int(number)]


def revert(i):
    if instructions[i] == 'jmp':
        instructions[i] = 'nop'
    elif instructions[i] == 'nop':
        instructions[i] = 'jmp'


def change(i):
    if instructions[i] == 'acc':
        return False
    else:
        revert(i)
    try:
        visited = []
        current = 0  # Starting index
        while current not in visited:
            visited += [current]
            to_do = instructions[current]
            if to_do == 'acc':
                current += 1
            elif to_do == 'jmp':
                current += value[current]
            else:
                current += 1
        revert(i)
        return False
    except IndexError:
        revert(i)
        return True


# Find the index of the observation that must be changed
j = 0
while not change(j):
    j += 1

# Change the instruction
revert(j)

# Run the changed code
accumulator = 0
go = 0
while go < len(instructions):
    to_do = instructions[go]
    if to_do == 'acc':
        accumulator += value[go]
        go += 1
    elif to_do == 'jmp':
        go += value[go]
    else:
        go += 1

print(accumulator)
