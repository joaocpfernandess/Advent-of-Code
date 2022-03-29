import functools
file = open('input.txt', 'r')
matrix = []
for line in file:
    matrix += [int(line)]
stop = False
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        if matrix[i]+matrix[j]==2020:
            stop = True
            break
    if stop:
        break

print(matrix[i])
print(matrix[j])
print(i, j)
print(matrix[i]+matrix[j])
print(matrix[i]*matrix[j])

print(functools.reduce(lambda a,b: a+b, [[1],[2],[3]]))
