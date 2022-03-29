file = open('input.txt', 'r')
valid = 0
for line in file:

    a = line.split()
    pos = ['', '']
    i = 0
    for p in a[0]:
        if p != '-':
            pos[i] += p
        else:
            i += 1
    pos = [int(pos[0])-1, int(pos[1])-1]
    letter = a[1][0]

    try:
        if (a[2][pos[0]] == letter and a[2][pos[1]] != letter) or (a[2][pos[0]] != letter and a[2][pos[1]] == letter):
            valid += 1
    except IndexError:
        if a[2][pos[0]] == letter:
            valid += 1

print(valid)