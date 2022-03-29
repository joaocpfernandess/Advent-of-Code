file = open('input.txt', 'r')
vals = []
diffs = []
for line in file:
    vals += [int(line)]
vals.sort()

diffsof1, diffsof3 = 0, 1
initdiff = vals[0]
if initdiff == 1:
    diffsof1 += 1
elif initdiff == 3:
    diffsof3 += 1


for j in range(len(vals)-1):
    n = vals[j+1]-vals[j]
    diffs += [n]
    if n == 1:
        diffsof1 += 1
    elif n == 3:
        diffsof3 += 1

print(diffsof1*diffsof3)

