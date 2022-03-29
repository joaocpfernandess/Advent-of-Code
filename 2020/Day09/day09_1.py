file = open('input.txt', 'r')

preamble = []
for _ in range(25):
    preamble += [int(file.readline())]


def sumoftwoQ(w,n):
    for i in range(len(w)-1):
        for j in range(i+1,len(w)):
            if w[i]+w[j] == n:
                return True
    return False


p = int(file.readline())
while sumoftwoQ(preamble, p):
    preamble = preamble[1:] + [p]
    p = int(file.readline())

print(p)
