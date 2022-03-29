from functools import *

file = open('input.txt', 'r')
ntrees = []
index_step = [1,3,5,7]
init_pos = file.tell()
n = len(file.readline())-1
for step in index_step:
    file.seek(init_pos)
    add = 0
    index = 0
    for line in file:
        if line[index % n] == '#':
            add += 1
        index += step
    ntrees += [add]

file.seek(init_pos)
index, add = 0, 0
for line in file:
    if line[index % n] == '#':
        add += 1
    index += 1
    file.readline()
ntrees += [add]

print(ntrees)
print(reduce(lambda x,y: x*y, ntrees))