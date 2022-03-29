file = open('input.txt', 'r')
ntrees = 0
index = 0
init_pos = file.tell()
n = len(file.readline())-1
file.seek(init_pos)
for line in file:
    if line[index % n] == '#':
        ntrees += 1
    index += 3
print(ntrees)

