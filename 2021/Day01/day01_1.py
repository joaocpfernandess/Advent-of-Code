file = open('input.txt', 'r')
i = int(file.readline())
linesread = 1
res = 0
while True:
    try:
        n = int(file.readline())
        linesread += 1
        if n > i:
            res += 1
        i = n
    except ValueError:
        break
print(res)
print(linesread)