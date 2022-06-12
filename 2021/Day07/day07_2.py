file = open('input.txt', 'r')

init = [int(n) for n in file.readline().split(',')]
min_init, max_init = min(init), max(init)
fuel = []

for p in range(min_init, max_init + 1):
    add_fuel = 0
    for i in init:
        add_fuel += 0.5*(abs(p-i)**2 + abs(p-i))
    fuel.append(add_fuel)

print(f'FINAL ANSWER: {min(fuel)}')
