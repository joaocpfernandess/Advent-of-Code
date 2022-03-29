def binlist_to_num(w):
    n = len(w)
    res = 0
    for i in range(n):
        res += w[n-1-i]*(2**i)
    return res

file = open('input.txt', 'r')
linesread = 0
pos = file.tell()
total = [0 for _ in file.readline()][:-1]
file.seek(pos)
for line in file:
    linesread += 1
    for i in range(len(line)-1):
        total[i] += int(line[i])
print(total)
print(linesread)
gamma_binlist, eps_binlist = [], []
for i in total:
    if i > linesread/2:
        gamma_binlist += [1]
        eps_binlist += [0]
    else:
        gamma_binlist += [0]
        eps_binlist += [1]

gamma_rate, eps_rate = binlist_to_num(gamma_binlist), binlist_to_num(eps_binlist)
print("Gamma rate: {}".format(gamma_rate))
print("Epislon rate: {}".format(eps_rate))
print("Result: {}".format(gamma_rate*eps_rate))




