file = open('input.txt', 'r')
i = int(file.readline())
j = int(file.readline())
k = int(file.readline())
linesread = 3
res = 0
while True:
    try:
        sum = i + j + k
        n = int(file.readline())
        sum_new = j + k + n
        linesread += 1
        if sum_new > sum:
            res += 1
        i = j
        j = k
        k = n
    except ValueError:
        break
print(res)
print(linesread)