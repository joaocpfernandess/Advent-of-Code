file = open('input.txt', 'r')
init_pos = file.tell()


def sumoftwoQ(w,n):
    for i in range(len(w)-1):
        for j in range(i+1,len(w)):
            if w[i]+w[j] == n:
                return True
    return False


preamble = []
for _ in range(25):
    preamble += [int(file.readline())]

target_index = 26
p = int(file.readline())
while sumoftwoQ(preamble, p):
    preamble = preamble[1:] + [p]
    p = int(file.readline())
    target_index += 1

print(p, target_index)

file.seek(init_pos)
alln = []
for line in file:
    alln += [int(line)]
alln.remove(p)
alln = list(filter(lambda x: x <= p, alln))

stop = False
winning_set = None
for j in range(1, len(alln)+1):
    for i in range(0,j):
        set1 = alln[i:j]
        set2 = alln[:i]+alln[j:]
        if sum(set1) == p:
            winning_set = set1
            stop = True
            break
        if sum(set2) == p:
            winning_set = set2
            stop = True
            break
    if stop:
        break

print(winning_set)
print(min(winning_set)+max(winning_set))
print(sum(winning_set))
print(p)










