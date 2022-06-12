file = open('input.txt', 'r')

count = 0
for line in file:
    output = line[:-1].split(' | ')[1].split(' ')
    count += len([i for i in output if len(i) in [2,3,4,7]])

print(f'FINAL ANSWER: {count}')

