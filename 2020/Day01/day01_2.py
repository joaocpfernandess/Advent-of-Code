file = open('input.txt', 'r')
matrix = []
for line in file:
    matrix += [int(line)]

i = 0
stop = False
while i<len(matrix)-2 and not stop:
    j=i+1
    while j<len(matrix)-1 and not stop:
        k=j+1
        while k<len(matrix) and not stop:
            if matrix[i]+matrix[j]+matrix[k]==2020:
                stop = True
            else:
                k += 1
        j += 1
    i += 1

print(matrix[i-1])
print(matrix[j-1])
print(matrix[k])
print(matrix[i-1]+matrix[j-1]+matrix[k])
print(i-1,j-1,k)
print(matrix[i-1]*matrix[j-1]*matrix[k])
