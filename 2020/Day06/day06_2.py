file = open('input.txt', 'r')

init_pos = file.tell()
file.read()
eof = file.read()
file.seek(init_pos)

nr_ans = []
for line in file:
    all = []
    while line != '\n' and line != eof:
        all += [line[:-1]]
        line = file.readline()
    possible = [le for le in all[0]]
    for set_ans in all[1:]:
        i = 0
        while i < len(possible):
            if possible[i] not in set_ans:
                possible.remove(possible[i])
            else:
                i += 1
    nr_ans += [len(possible)]
    
print(nr_ans)
print(sum(nr_ans))


