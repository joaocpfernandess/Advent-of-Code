file = open('input.txt', 'r')

init_pos = file.tell()
file.read()
eof = file.read()
file.seek(init_pos)

nr_ans = []
for line in file:
    ans = []
    all = ''
    while line != '\n' and line != eof:
        all += line[:-1]
        line = file.readline()
    for q in all:
        if q not in ans:
            ans.append(q)
    nr_ans += [len(ans)]
print(nr_ans)
print(sum(nr_ans))
