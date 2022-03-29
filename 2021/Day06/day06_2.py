file = open('input.txt', 'r')
"""
class Lanternfish:

    def __init__(self, days):
        self.days = days

    def sonsindays(self, d):
        sons = 0
        for j in range(d):
            self.days = self.days - 1 if self.days > 0 else 6
            if self.days == 6:
                sons += 1
                b = Lanternfish(8)
                sons += b.sonsindays(d-j)
        return sons



res = 0
for l in init:
    fish = Lanternfish(l)
    res += fish.sonsindays(256)
print(res)

def sons(n, days):
    first_son = days - n - 1
    days_of_birth = [first_son-7*i for i in range(int(first_son/7)+1)]
    if first_son > 0:
        return int((days-n-1)/7)+1+sum([sons(8, d) for d in days_of_birth])
    else:
        return 0

init = [int(n) for n in file.readline().split(',')]
res, nfish = 0, 0
for n in init:
    res += sons(n, 256)
    print(f"FISH {nfish}: {res}")
print(res)
"""

init = [int(n) for n in file.readline().split(',')]
print(init)
for k in range(256):
    print(k)
    add = [8 for i in init if i == 0]
    init = list(map(lambda x: x-1 if x > 0 else 6, init))
    init += add
print(len(init))

