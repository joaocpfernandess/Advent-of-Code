needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def has_attr(passport):
    found_attr = []
    for attr in passport:
        add = ''
        for l in attr:
            if l == ':':
                break
            else:
                add += l
        found_attr += [add]
    v = True
    for check in needed:
        if check not in found_attr:
            v = False
            break
    return v


def valid_data(passport):
    keyval = []
    for attr in passport:
        add, i = ['', ''], 0
        for l in attr:
            if l == ':':
                i = 1
            else:
                add[i] += l
        keyval += [add]
    v = True
    yr_limits = [[1920, 2002], [2010, 2020], [2020, 2030]]
    for check in keyval:

        if check[0] in ['byr', 'iyr', 'eyr']:
            try:
                yr, i = int(check[1]), ['byr', 'iyr', 'eyr'].index(check[0])
                if yr < yr_limits[i][0] or yr > yr_limits[i][1]:
                    v = False
                    break
            except ValueError:
                v = False
                break

        elif check[0] == 'hgt':
            i = 0
            nr = ''
            while i < len(check[1]) and check[1][i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                nr += check[1][i]
                i += 1
            unit = ''
            while i < len(check[1]):
                unit += check[1][i]
                i += 1
            try:
                nr = int(nr)
                if unit == 'cm':
                    if nr < 150 or nr > 193:
                        v = False
                        break
                elif unit == 'in':
                    if nr < 59 or nr > 76:
                        v = False
                        break
                else:
                    v = False
                    break
            except ValueError:
                v = False
                break

        elif check[0] == 'hcl':
            j = 1
            try:
                while j < 7 and check[1][j] in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    j += 1
                v = (j == 7) and (check[1][0] == '#')
                if not v:
                    break
            except IndexError:
                v = False
                break

        elif check[0] == 'ecl':
            if check[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                v = False
                break

        elif check[0] == 'pid':
            try:
                nr = int(check[1])
                if len(check[1]) != 9:
                    v = False
                    break
            except ValueError:
                v = False
                break

        else:
            pass

    return v


file = open('input.txt', 'r')

init_pos = file.tell()
file.read()
eof = file.read()
file.seek(init_pos)

passports = []
for line in file:
    stuff = []
    while line != '\n' and line != eof:
        stuff += line.split()
        line = file.readline()
    passports += [stuff]

valid = 0
for p in passports:
    if has_attr(p):
        if valid_data(p):
            valid += 1
print(valid)
