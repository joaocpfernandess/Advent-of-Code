def binlist_to_num(w):
    n = len(w)
    res = 0
    for i in range(n):
        res += w[n-1-i]*(2**i)
    return res

file = open('input.txt', 'r')
matrix = []
for line in file:
    add = []
    for i in range(len(line)-1):
        add += [int(line[i])]
    matrix += [add]

print("--------- OXYGEN -----------")
j = 0
res_ogr = matrix
while len(res_ogr)!=1:
    n1 = len([l for l in res_ogr if l[j]==1])
    print("n1={}; j={}; len={} --- 1 or 0? {}".format(n1, j, len(res_ogr), 1 if n1 >= len(res_ogr)/2 else 0))
    if n1 >= len(res_ogr)/2:
        res_ogr = [r for r in res_ogr if r[j]==1]
    else:
        res_ogr = [r for r in res_ogr if r[j]==0]
    j += 1

print(res_ogr)
ogr = binlist_to_num(res_ogr[0])
print(ogr)

print("--------- CO2 -----------")
k = 0
res_co2 = matrix
while len(res_co2)!=1:
    n1 = len([l for l in res_co2 if l[k]==1])
    print("n1={}; j={}; len={} --- 1 or 0? {}".format(n1, k, len(res_co2), 0 if n1 <= len(res_co2) / 2 else 1))
    if n1 >= len(res_co2)/2:
        res_co2 = [r for r in res_co2 if r[k]==0]
    else:
        res_co2 = [r for r in res_co2 if r[k]==1]
    k += 1

print(res_co2)
co2 = binlist_to_num(res_co2[0])
print(co2)
""""""
print(co2*ogr)