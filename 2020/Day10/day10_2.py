file = open('input.txt', 'r')

vals = []
for line in file:
    vals += [int(line)]
vals.sort()
"""
vals = [16,10,15,5,1,11,7,19,6,12,4]
vals.sort()
"""
diffs = [vals[0]]   # Never occurs differences of 2; only 1 and 3
for j in range(len(vals)-1):
    n = vals[j+1]-vals[j]
    diffs += [n]

"""
# Function that finds all subsets containing only 1, 2 or 3's that add up to p.
def subsets123(p):
    if p == 1 or p == 0:
        return 1
    elif p == 2:
        return 2
    elif p == 3:
        return 4
    else:
        return (p-1)*subsets123(p-1)+(p-2)*subsets123(p-2)+1


print(subsets123(10))
print(subsets123(5))
"""

# KEY POINT: every pair that has a difference of 3 is ALWAYS included.
# The maximum of vals is also included (since the final adapter is +3 than the max)

sequencesof1, j = [], 0
while j < len(diffs):
    seq = 0
    while j < len(diffs) and diffs[j] == 1:
        seq += 1
        j += 1
    if seq > 0:
        sequencesof1 += [seq]
    j += 1


res = 1
for n in sequencesof1:
    res *= [1,2,4,7][[1,2,3,4].index(n)]
print(sequencesof1)
print(res)
