file = open('input.txt', 'r')
init = [int(n) for n in file.readline().split(',')]
"""
print(init)
for _ in range(80):
    add = [8 for i in init if i == 0]
    init = list(map(lambda x: x-1 if x > 0 else 6, init))
    init += add
print(len(init)) # 380612 (right answer)

"""
def sons(n, days):
    first_son = days - n - 1
    #print(first_son)
    days_of_birth = [first_son-7*i for i in range(int(first_son/7)+1)]
    print(days_of_birth)
    if first_son > 0:
        return int((days-n-1)/7)+1+sum([sons(8, d) for d in days_of_birth])
    else:
        return 0

#init = [int(n) for n in file.readline().split(',')]
res, nfish = 0, 1
print(sons(3, 80))
"""for n in init:
    res += sons(n, 80)
    print(f"FISH {nfish}: {res}")
    nfish += 1
print(res) # 361407 (wrong)"""
